import sqlite3


def create_table_product() -> None:
	"""
	Создать таблицу product, для хранения товаров.
	Колонки: id, id чата, артикул товара, размер, цена.
	"""
	connection = sqlite3.connect('bot.sql')
	cursor = connection.cursor()
	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS product (
		id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		chat_id INTEGER NOT NULL,
		product_item INTEGER NOT NULL,
		size VARCHAR(20),
		price INTEGER
		);
		"""
	)
	connection.commit()
	cursor.close()
	connection.close()


def add_product(chat_id: int, product_item: int, size_name: str, price: int) -> None:
	"""
	Добавить товар в таблицу product.

	:param chat_id: id чата с пользователем
	:type chat_id: int

	:param product_item: Артикул товара
	:type product_item: int

	:param size_name: Размер
	:type size_name: str

	:param price: Цена
	:type price: int

	:return: None
	"""
	connection = sqlite3.connect('bot.sql')
	cursor = connection.cursor()
	cursor.execute(
		"""
		INSERT INTO product
		(chat_id, product_item, size, price)
		VALUES
		(?, ?, ?, ?);
		""",
		(chat_id, product_item, size_name, price,)
	)
	connection.commit()
	cursor.close()
	connection.close()
