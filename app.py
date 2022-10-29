from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#アクセストークンの入力
line_bot_api = LineBotApi('7sId6bqX6NjXY4JVJklhFOF40yz5H37Qv8oi/7af6Tw6Q1nbublh9AZYLQJxHGleIvl4doeltEU7j17U2Fw4RuYehks9+PV8Dtp6pb9LOj47DB/qK+Jpw9HyF7IfnRcY3+QeHZPd6qp9bT1uENRXmwdB04t89/1O/w1cDnyilFU=')
#チャンネルの秘密（チャンネルシークレット）を入力
handler = WebhookHandler('1c6e051751dd565bbc4e4bd102965a6c')

#テスト用
@app.route("/")
def test():
    return 'OK'

# Webhook URLの最後に /callback を付け足す
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

from time import time
#この時点でstartを初期化しておく
start = 0

@handler.add(MessageEvent, message=TextMessage)
def handle_message_1(event):
    if event.message.text == "ありがとう":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"余裕っすよ！ \n いつでも助けたる！ \n ( ˘ω˘)ドヤ")) 
    elif event.message.text == "作業開始":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"了解！ \n 時間管理は任せな！"))
        global start
        start = time()
    elif event.message.text == "作業終了":
        end = time()
        difference = int(end - start)
        #割り算の整数部分の出力
        hour = difference//3600
        #％は余りを出力
        minute = (difference%3600)//60
        second = difference%60
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"お疲れ様！！ \n 作業時間は{hour}時間{minute}分{second}秒でしたよ！"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"あなたは、「{event.message.text}」と言いました。 \n 現在、このワードは準備中です。"))

if __name__ == "__main__":
    app.run()