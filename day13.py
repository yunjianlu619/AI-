import json
import requests

# 分镜列表
shot_list = [
    "国企楼下，问天被领导一把推开，手中仲裁书被捏皱，低机位近景，情绪压抑",
    "出租屋内，问天颓然坐下倒空钱包，手机弹出房租短信，室内冷光，中景",
    "出租屋房门打开，南宫清鸢走入上前抱住问天、眼眶泛红，中景，暖光"
]

def get_ai_image(prompt):
    url = "你的API地址"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "你的token"
    }
    payload = {
        "prompt": prompt,
        "size": "1024x1024"
    }
    try:
        resp = requests.post(url, headers=headers, json=payload)
        res_data = resp.json()
        if res_data.get("code") == 200:
            return res_data["img_url"]
        else:
            return f"失败：{res_data.get('msg')}"
    except Exception as e:
        return f"请求异常：{e}"

if __name__ == "__main__":
    result_save = []
    for shot in shot_list:
        print(f"正在生成：{shot}")
        img_link = get_ai_image(shot)
        result_save.append({
            "prompt": shot,
            "img_url": img_link
        })
    # 写入文件
    with open("shot_result.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(result_save, ensure_ascii=False, indent=2))
    print("\n✅全部完成，结果已保存 shot_result.txt")
