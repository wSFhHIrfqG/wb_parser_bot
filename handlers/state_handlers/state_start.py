import telebot.types

from loader import bot
from states.user_states import UserStates
import messages


@bot.message_handler(state=UserStates.start)
def keyboard_button_clicked(message: telebot.types.Message):
	if message.text == 'Поиск товара 🔍':
		bot.set_state(message.chat.id, UserStates.product_item)
		bot.send_message(
			message.chat.id,
			messages.dialogue.ask_product_item_text(message),
			reply_markup=telebot.types.ReplyKeyboardRemove()
		)
	else:
		bot.send_message(
			message.chat.id,
			messages.dialogue.incorrect_start_action_text(message),
			reply_markup=telebot.types.ReplyKeyboardRemove()
		)
