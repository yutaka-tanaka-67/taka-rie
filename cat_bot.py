from cmath import inf
import json
import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info_cat.json', 'r')
info = json.load(file)
#webhook_url = "{https://yutaka-dx.com}"
#requests.post(webhook_url)

u_token = info["TOKEN"]
line_bot_api = LineBotApi(u_token)

def main():
    u_id = info["SECLET"]
    test_messages = TextSendMessage(text="テストです \n 以上")
    line_bot_api.push_message(u_id, messages=test_messages)
    
    
if __name__ == "__main__":
    main()
    
