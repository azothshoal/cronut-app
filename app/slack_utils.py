from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Replace with your actual Slack bot token
SLACK_BOT_TOKEN = "your-slack-bot-token"
client = WebClient(token=SLACK_BOT_TOKEN)

def send_message(user_id: str, message: str):
    try:
        response = client.chat_postMessage(channel=user_id, text=message)
        return response["ts"]
    except SlackApiError as e:
        print(f"Error sending message: {e}")
