from loader import bot
import messages


@bot.callback_query_handler(func=lambda call: call.data.startswith('size'))
def size(call):
	product_item = int(call.data.split(':')[1])
	size_name = call.data.split(':')[2]

	with bot.retrieve_data(call.message.chat.id) as data:
		product_data = data[product_item]

		product_card = messages.product_card.ProductCard(
			product_item=product_item, product_data=product_data, size_name=size_name
		)

		bot.edit_message_caption(
			product_card.caption(),
			call.message.chat.id,
			message_id=call.message.message_id,
			parse_mode='html',
			reply_markup=product_card.markup()
		)
