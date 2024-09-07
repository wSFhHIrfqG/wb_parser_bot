import telebot.types

from loader import bot
from states.user_states import UserStates
import parse
from parse import exceptions
import messages


@bot.message_handler(state=UserStates.product_item, is_digit=True)
def get_product_info(message: telebot.types.Message):
	bot.set_state(message.chat.id, UserStates.start)

	product_item = int(message.text)
	product = parse.wb_product.WBProduct(product_item)

	try:
		product_data = product.product_data()
	except parse.exceptions.ProductNotExistsError:
		messages.dialogue.product_not_found_text(message)
		return

	with bot.retrieve_data(message.from_user.id) as data:
		data[product_item] = product_data

	sizes = product_data.get('sizes')

	if len(sizes) == 1:  # У товара только один размер
		product_card = messages.product_card.ProductCard(
			product_item=product_item, product_data=product_data, size_name=''
		)
	else:
		product_card = messages.product_card.ProductCard(
			product_item=product_item, product_data=product_data,
		)

	bot.send_photo(
		message.chat.id,
		product_card.image_link,
		product_card.caption(),
		parse_mode='html',
		reply_markup=product_card.markup()
	)
