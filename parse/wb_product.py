import requests


class WBProduct:

	def __init__(self, product_item: int):
		if not isinstance(product_item, int):
			raise TypeError('product item must be int, not %s', type(product_item).__name__)
		self.product_item = product_item

	def __get_response(self) -> requests.Response:
		pass

	def product_data(self) -> dict | None:
		pass

	def product_image_url(self) -> str:
		pass
