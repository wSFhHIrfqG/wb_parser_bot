import telebot.types

from loader import bot
from states.user_states import UserStates
import database
import messages
import keyboards


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

	total_price = None
	for size in product_data.get('sizes'):
		if size.get('name') == size_name:
			price_info = size.get('price', {})
			if price_info:
				total_price = price_info.get('total')
			break

	database.edit.add_product(
		chat_id=call.message.chat.id, product_item=product_item, size_name=size_name, price=total_price
	)

	bot.reply_to(
		call.message,
		messages.dialogue.product_added_text(call.message),
		reply_markup=keyboards.reply.start_menu.start_menu_markup(),
		parse_mode='html'
	)
