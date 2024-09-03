from telebot import TeleBot
from telebot import StateMemoryStorage
from telebot import custom_filters

from config_data import config

state_storage = StateMemoryStorage()
bot = TeleBot(config.TOKEN, state_storage=state_storage)

bot.add_custom_filter(custom_filters.StateFilter(bot))
