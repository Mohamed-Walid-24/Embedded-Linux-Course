import requests
import json

response = requests.get("https://api.ipify.org/?format=json")

print(response.status_code)
# 200 --> Success!
# 404 --> Not Found!

print(response.content.decode("utf-8"))
ip = json.loads(response.content.decode("utf-8"))["ip"]

link = f"https://ipinfo.io/{ip}/geo"

res = requests.get(link)
print(res.content.decode("utf-8"))
