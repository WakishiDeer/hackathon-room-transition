from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os
import requests

YOUR_CHANNEL_ACCESS_TOKEN="H8FPKMz/Wn9/G1Z2gNFeMMlL9IIzzmFG7UoNekfPgGFQ6mTfbTsOG9Ocr0y2ZMHQkIjWBoHagD1U3nQCNrvyWdyrwucSJctPoztve0wcJwSB7zbeGUX0Lg17g0wucSJctPoztve0wcJwSB7zbeGUX0Lg17g6wucSJctPoztve0wcJwSB7zbeGUX0Lg17g6"
YOUR_CHANNEL_SECRET="413ee572142077a82cab81a410043c9c"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def webhook():
    # リクエストヘッダーから署名検証のための値を取得します。
    signature = request.headers['X-Line-Signature']
 
    # リクエストボディを取得します。
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
　# 署名を検証し、問題なければhandleに定義されている関数を呼び出す。
    try:
        handler.handle(body, signature)
　# 署名検証で失敗した場合、例外を出す。
    except InvalidSignatureError:
        abort(400)
　# handleの処理を終えればOK
    return 'OK'

