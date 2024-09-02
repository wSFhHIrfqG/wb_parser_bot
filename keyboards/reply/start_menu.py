from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def start_menu_markup():
	markup = ReplyKeyboardMarkup(resize_keyboard=True)

	btn1 = KeyboardButton('Поиск товара 🔍')

	markup.row(btn1)

	return markup
