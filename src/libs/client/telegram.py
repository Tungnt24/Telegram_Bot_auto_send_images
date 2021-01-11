import telebot
from src.configuration.teleconfig import BotConfig


class Telegram:
    def __init__(self):
        self.bot = telebot.TeleBot(BotConfig.token)

    def send_image(self, group_id, image):
        self.bot.send_photo(group_id, image)

    def send_message(self, group_id, message):
        self.bot.send_message(group_id, message)
