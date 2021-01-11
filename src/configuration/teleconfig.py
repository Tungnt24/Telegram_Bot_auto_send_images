import os
from dotenv import load_dotenv

load_dotenv()


class BotConfig:
    token = os.getenv("TOKEN")
    group_id = os.getenv("GROUP_ID")
