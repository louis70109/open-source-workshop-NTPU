from linebot.v3 import WebhookHandler
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ShowLoadingAnimationRequest
)
import json
import os

# 使用環境變量讀取憑證
CHANNEL_SECRET = os.getenv('ChannelSecret', None)
CHANNEL_ACCESS_TOKEN = os.getenv('ChannelAccessToken', None)

handler = WebhookHandler(CHANNEL_SECRET)
configuration = Configuration(
    access_token=CHANNEL_ACCESS_TOKEN
)

def linebot(request):
    try:
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        
        event = json_data['events'][0]
        reply_token = event['replyToken']
        user_id = event['source']['userId']
        msg_type = event['message']['type']

        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            
            if msg_type == 'text':
                msg = event['message']['text']
                line_bot_api.show_loading_animation(ShowLoadingAnimationRequest(
                    chatId=user_id, loadingSeconds=20))

                if msg == '!清空':
                    reply_msg = '已清空'
                    # fdb.delete(user_chat_path, None)
                elif msg == '!摘要':
                    reply_msg = msg # test
                else:
                    reply_msg = "哈囉你好嗎"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[
                            TextMessage(text=reply_msg),
                        ]
                    )
                )
            else:
                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[
                            TextMessage(text='你傳的不是文字訊息喔'),
                        ]
                    )
                )
        return 'OK'
    
    except Exception as e:
        # 記錄錯誤詳情
        print(f"An error occurred: {e}")
        return 'Error'
