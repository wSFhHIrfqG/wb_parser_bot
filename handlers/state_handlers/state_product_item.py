import telebot.types

from loader import bot
from states.user_states import UserStates
import parse.wb_product
import parse.models
import parse.exceptions
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
