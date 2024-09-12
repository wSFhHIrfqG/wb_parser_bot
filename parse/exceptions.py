class ProductNotExistsError(Exception):
	"""Товар не найден"""

	def __init__(self, product_item):
		self.product_item = product_item

	def __str__(self):
		return f'Товар с данным артикулом не найден: {self.product_item}'
