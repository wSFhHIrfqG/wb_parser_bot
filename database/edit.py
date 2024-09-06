import sqlite3


def create_table_product():
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


def add_product(chat_id: int, product_item: int, size_name: str, price: int):
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
