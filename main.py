from linebot.v3 import (
    WebhookHandler
)
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

# Load environment variables
secret = os.getenv('ChannelSecret', None)
token = os.getenv('ChannelAccessToken', None)

# Initialize Line webhook handler and configuration
handler = WebhookHandler(secret)
configuration = Configuration(
    access_token=token
)

# Define your Line bot function
def linebot(request):
    try:
        # Get request body data
        body = request.get_data(as_text=True)
        json_data = json.loads(body)

        # Validate Line signature
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)

        # Extract event data
        event = json_data['events'][0]
        reply_token = event['replyToken']
        user_id = event['source']['userId']
        msg_type = event['message']['type']
        msg = event.get('message', {}).get('text', None)

        # Initialize Line Messaging API client
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)

            # Handle different message types
            if msg_type == 'text':
                if msg == '!清空':
                    reply_msg = '已清空'
                    # Handle clear command
                elif msg == '!摘要':
                    reply_msg = msg  # Placeholder for summary command
                else:
                    reply_msg = "哈囉你好嗎"
            else:
                reply_msg = '你傳的不是文字訊息喔'

            # Send reply message
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=reply_token,
                    messages=[
                        TextMessage(text=reply_msg),
                    ]
                )
            )
    except Exception as e:
        # Handle exceptions
        detail = e.args[0]
        print(f"Error: {detail}")

    return 'OK'
