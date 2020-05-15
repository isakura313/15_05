import requests

payload = {"text": "ozon"}

r  = requests.get("https://httpbin.org/get", params=payload)
print(r.text)