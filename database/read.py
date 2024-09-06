import sqlite3


def all_products():
	connection = sqlite3.connect('bot.sql')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM product;')
	data = cursor.fetchall()
	cursor.close()
	connection.close()
	return data
