import requests

def api_get(url: str):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        print(f"✅ 请求成功，状态码：{resp.status_code}")
        return resp.json()
    except requests.exceptions.RequestException as err:
        print(f"❌ 网络请求异常：{err}")
        return None

def read_shots(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    shots_text = read_shots("shot_list.txt")
    print("本地读取分镜：\n", shots_text)
    test_api = "https://jsonplaceholder.typicode.com/todos/1"
    res_data = api_get(test_api)
    if res_data:
        print("接口返回：", res_data)
