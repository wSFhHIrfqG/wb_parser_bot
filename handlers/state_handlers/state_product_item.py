import telebot.types

from loader import bot
from states.user_states import UserStates
import parse
from parse import exceptions
import messages


@bot.message_handler(state=UserStates.product_item, is_digit=True)
def get_product_info(message: telebot.types.Message) -> None:
	"""
	Получен артикул товара.

	:param message: Сообщение
	:return: None
	"""
	bot.set_state(message.chat.id, UserStates.start)

	product_item = int(message.text)

	with bot.retrieve_data(message.from_user.id) as data:
		product = parse.wb_product.WBProduct(product_item)

		# Получаем данные товара
		try:
			product_data = product.product_data()
		except parse.exceptions.ProductNotExistsError:
			bot.send_message(
				message.chat.id,
				messages.dialogue.product_not_found_text(message),
				parse_mode='html'
			)
			return

		# Сохраняем данные в retrieve data
		data[product_item] = product_data

		# Создаем карточку товара
		sizes = product_data.get('sizes')
		if len(sizes) == 1:  # У товара только один размер
			product_card = messages.product_card.ProductCard(
				product_item=product_item, product_data=product_data, size_name=''
			)
		else:
			product_card = messages.product_card.ProductCard(
				product_item=product_item, product_data=product_data,
			)

		# Отправляем карточку товара
		bot.send_photo(
			message.chat.id,
			product_card.image_link,
			product_card.caption(),
			parse_mode='html',
			reply_markup=product_card.markup()
		)


@bot.message_handler(state=UserStates.product_item, is_digit=False)
def incorrect_product_item(message: telebot.types.Message) -> None:
	"""
	Артикул товара введен некорректно.

	:param message: Сообщение
	:return: None
	"""
	bot.send_message(
		message.chat.id,
		messages.dialogue.incorrect_product_item_text(message),
		parse_mode='html'
	)
