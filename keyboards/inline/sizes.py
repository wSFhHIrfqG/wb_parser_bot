from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def product_sizes_markup(product_item: int, sizes: list) -> InlineKeyboardMarkup:
	"""
	Клавиатура для выбора размера.

	:param product_item: Артикул товара
	:type product_item: int

	:param sizes: Размер
	:type sizes: str

	:return: Клавиатура InlineKeyboardMarkup
	"""
	markup = InlineKeyboardMarkup(row_width=4)

	buttons = []
	for size in sizes:
		size_name = size.get('name')
		btn = InlineKeyboardButton(size_name, callback_data=f'size:{product_item}:{size_name}')
		buttons.append(btn)

	markup.add(*buttons)
	return markup
