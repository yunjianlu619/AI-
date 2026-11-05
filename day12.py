# Day12 requests Post + json传参学习
import requests

def api_post(url,post_data):
    try:
        resp=requests.post(
            url=url,
            json=post_data, # 自动把python字典转为json
            timeout=20
        )
        resp.raise_for_status()
        print(f"✅ POST请求成功，状态码：{resp.status_code}")
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ POST请求异常：{e}")
        return None

if __name__ == "__main__":
    # 免费测试POST接口，用来练手
    test_url="https://jsonplaceholder.typicode.com/posts"
    # 这就是传给接口的json参数（Python字典
    prompt_data={"title": "漫剧分镜绘图",
        "body": "问天推开国企大门，低机位近景，压抑冷色调",
        "userId": 1
    }

    result=api_post(test_url,prompt_data)
    if result:
        print("接口返回结果：")
        print(result)

# 【模板：AI绘图POST参数样板，以后直接改】
draw_param = {
    "prompt": "南宫问天，中景，暖光，南宫清鸢拥抱问天，眼眶泛红，二次元漫剧画风",
    "negative_prompt": "模糊，畸形，多余肢体，低画质",
    "width": 1024,
    "height": 768,
    "style": "anime"
}
