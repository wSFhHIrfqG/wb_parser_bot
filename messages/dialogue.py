import telebot.types


def start_dialogue_text(message: telebot.types.Message):
	text = """
	👋 Привет, это бот для отслеживания товаров на WILDBERRIES!
	
	<b>Как это работает?</b>
	
	— Чтобы найти товар нажмите "Поиск товара"
	
	— Отправьте артикул
	
	— Выберите размер и добавьте товар в список отслеживания
	
	— Готово! Вы получите уведомление, когда цена на товар будет снижена или он появится в наличии
	"""

	return text


def ask_product_item_text(message: telebot.types.Message):
	text = "Введите артикул товарa"
	return text


def incorrect_start_action_text(message: telebot.types.Message):
	text = "Выберите действие из указанных на клавиатуре"
	return text


def product_not_found_text(message: telebot.types.Message):
	text = f'Товар с артикулом {message.text} не найден'
	return text
