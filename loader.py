from telebot import TeleBot
from telebot import StateMemoryStorage

from config_data import config

state_storage = StateMemoryStorage()
bot = TeleBot(config.TOKEN, state_storage=state_storage)
