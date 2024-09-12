import sqlite3


def all_products() -> list[tuple[int, int, int, str, int]]:
	"""
	Получить все записи в таблице product.

	:return: Содержание таблицы product
	"""
	connection = sqlite3.connect('bot.sql')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM product;')
	data = cursor.fetchall()
	cursor.close()
	connection.close()
	return data
