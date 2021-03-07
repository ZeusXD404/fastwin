import json
import requests
import time

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    return res_json["tunnels"][0]["public_url"][6:]

while True:
	print(get_ngrok_url())
	time.sleep(8)
