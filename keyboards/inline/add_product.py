from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_product_markup(product_item: int, size_name: str = '') -> InlineKeyboardMarkup:
	"""
	Клавиатура с кнопкой "добавить товар".

	:param product_item: Артикул товара
	:type product_item: int

	:param size_name: Размер
	:type size_name: str

	:return: Клавиатура InlineKeyboardMarkup
	"""
	markup = InlineKeyboardMarkup()

	btn = InlineKeyboardButton('Добавить товар', callback_data=f'add_product:{product_item}:{size_name}')

	markup.row(btn)

	return markup
