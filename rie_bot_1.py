from flask import Flask, request, abort
from flask.logging import create_logger
from cmath import inf
import os
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage

app = Flask(__name__)
log = create_logger(app)

#変数化
my_token = os.environ["FtFzXBcMHF20K8mEONA8Cc6YfwG9S7p95qzetbLrB6V9ay/HWshGV7jSeFvOQH5RIvl4doeltEU7j17U2Fw4RuYehks9+PV8Dtp6pb9LOj4qFSXOL0cHHuaB1anS6sEcmrASOO1YbLeVEEj7sA4rxQ1dB0il=8rxQ1dB0"]
my_id = os.environ["3ca765155e4717c9cb5436698e6018d6"]

#情報を設定
line_bot_api = LineBotApi(my_token)
handler = WebhookHandler(my_id)


@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']
 
    # リクエストボディを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #log.info("Request body: " + body)
 
    # 署名を検証し、問題なければhandleに定義されている関数を呼ぶ
    try:
        handler.handle(body, signature)
        handler.handle(body, signature)
    # 署名検証で失敗した場合、例外を出す
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    # handleの処理を終えればOK
    return 'OK'
    

    
