from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_product_markup(product_item: int, size_name: str = ''):
	markup = InlineKeyboardMarkup()

	btn = InlineKeyboardButton('Добавить товар', callback_data=f'add_product:{product_item}:{size_name}')

	markup.row(btn)

	return markup
