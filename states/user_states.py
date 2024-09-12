from telebot.handler_backends import State, StatesGroup


class UserStates(StatesGroup):
	start = State()  # Начальное меню
	product_item = State()  # Ожидается артикул товара
