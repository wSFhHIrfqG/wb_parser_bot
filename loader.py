from telebot import TeleBot
from telebot import StateMemoryStorage
from telebot import custom_filters

from config_data import config
import database

state_storage = StateMemoryStorage()
bot = TeleBot(config.TOKEN, state_storage=state_storage)

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

database.edit.create_table_product()
