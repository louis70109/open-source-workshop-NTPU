from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    TextSendMessage
)
import json
import os
import requests
from PIL import Image
from io import BytesIO
from firebase import firebase
import google.generativeai as genai

# 使用環境變量讀取憑證
secret = os.getenv('ChannelSecret', None)
token = os.getenv('ChannelAccessToken', None)

handler = WebhookHandler(secret)
line_bot_api = LineBotApi(token)

def linebot(request):
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    try:
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)

        event = json_data['events'][0]
        reply_token = event['replyToken']
        user_id = event['source']['userId']
        msg_type = event['message']['type']

        if msg_type == 'text':
            msg = event['message']['text']
            if msg == '!清空':
                reply_msg = '已清空'
            elif msg == '!摘要':
                reply_msg = msg # test
            else:
                reply_msg = "哈囉你好嗎"

            line_bot_api.reply_message(
                reply_token,
                messages=[TextSendMessage(text=reply_msg)]
            )
        else:
            line_bot_api.reply_message(
                reply_token,
                messages=[TextSendMessage(text='你傳的不是文字訊息喔')]
            )

    except Exception as e:
        detail = e.args[0]
        print(detail)
    return 'OK'
