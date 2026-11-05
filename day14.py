import json
import requests

def read_script_txt(file_path):
    """读取本地剧本txt，返回分镜列表"""
    shot_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                # 跳过空行
                if line:
                    shot_list.append(line)
        return shot_list
    except FileNotFoundError:
        print("⚠️ 错误：找不到剧本文件！检查文件名和路径")
        return []
    except Exception as e:
        print(f"⚠️ 文件读取异常：{e}")
        return []


def build_prompt(shot_text):
    """给原始分镜加上画风前缀，组装成绘图prompt"""
    style_prefix = "漫剧，精致二次元，电影运镜，光影细腻，"
    full_prompt = style_prefix + shot_text
    return full_prompt


def test_post_api(test_prompt):
    """POST连通性测试函数，你可以填入你的测试API"""
    # =========这里换成你的测试接口地址=========
    api_url = "https://xxx/test-api"
    token = "填入你的token"
    # =========================================
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    payload = {
        "prompt": test_prompt,
        "size": "1024x1024"
    }
    try:
        resp = requests.post(api_url, headers=headers, json=payload, timeout=15)
        result = resp.json()
        return result
    except requests.exceptions.RequestException as e:
        return {"code": -1, "msg": f"网络请求失败：{str(e)}"}
    except json.JSONDecodeError:
        return {"code": -2, "msg": "接口返回不是合法JSON"}


if __name__ == "__main__":
    # 剧本文件，和py放在同一个文件夹
    script_file = "script.txt"
    shots = read_script_txt(script_file)

    if not shots:
        print("没有读到有效分镜，程序退出")
    else:
        print(f"✅一共读取到 {len(shots)} 条分镜\n")
        all_result = []
        for shot in shots:
            prompt = build_prompt(shot)
            print(f"📝原始分镜：{shot}")
            print(f"🎨组装prompt：{prompt}")
            api_res = test_post_api(prompt)
            print(f"📩接口返回：{api_res}\n")
            all_result.append({
                "shot": shot,
                "prompt": prompt,
                "api_response": api_res
            })

        # 保存全部结果
        with open("week2_result.txt", "w", encoding="utf-8") as out_f:
            out_f.write(json.dumps(all_result, ensure_ascii=False, indent=2))
        print("✅全部处理完成，结果保存到 week2_result.txt")
