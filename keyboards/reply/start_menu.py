from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def start_menu_markup() -> ReplyKeyboardMarkup:
	"""
	Клавиатура для выбора начального действия.

	:return: Клавиатура ReplyKeyboardMarkup
	"""
	markup = ReplyKeyboardMarkup(resize_keyboard=True)

	btn1 = KeyboardButton('Поиск товара 🔍')

	markup.row(btn1)

	return markup
