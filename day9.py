import requests

try:
    resp = requests.get("https://www.baidu.com", timeout=10)
    print("✅ 请求成功，状态码：", resp.status_code)
except Exception as e:
    print("❌ 请求出错：", e)




