import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/cronut')
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN', 'your-slack-bot-token')
