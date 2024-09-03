import telebot.types

from loader import bot
from states.user_states import UserStates
import messages
import keyboards


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
	bot.set_state(message.chat.id, UserStates.start)
	bot.send_message(
		message.chat.id,
		messages.dialogue.start_dialogue_text(message),
		reply_markup=keyboards.reply.start_menu.start_menu_markup(),
		parse_mode='html'
	)
