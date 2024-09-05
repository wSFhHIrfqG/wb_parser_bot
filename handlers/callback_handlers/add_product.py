import telebot.types

from loader import bot
from states.user_states import UserStates
import messages


@bot.callback_query_handler(func=lambda call: call.data.startswith('add_product'))
def add_product(call: telebot.types.CallbackQuery):
	bot.set_state(call.message.chat.id, UserStates.start)

	product_item = int(call.data.split(':')[1])
	size_name = call.data.split(':')[2]

	with bot.retrieve_data(call.from_user.id) as data:
		product_data = data.get(product_item)

	# Убираем кнопку
	product_card = messages.product_card.ProductCard(
		product_item=product_item, product_data=product_data, size_name=size_name
	)
	bot.edit_message_caption(
		product_card.caption(),
		call.message.chat.id,
		call.message.message_id,
		parse_mode='html',
	)
