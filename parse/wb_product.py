import requests


class WBProduct:

	def __init__(self, product_item: int):
		if not isinstance(product_item, int):
			raise TypeError('product item must be int, not %s', type(product_item).__name__)
		self.product_item = product_item

	def __get_response(self) -> requests.Response:
		headers = {
			'Accept': '*/*',
			'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
			'Connection': 'keep-alive',
			'Origin': 'https://www.wildberries.ru',
			'Referer': f'https://www.wildberries.ru/catalog/{self.product_item}/detail.aspx',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'cross-site',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition Yx GX)',
			'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
		}

		params = {
			'appType': '1',
			'curr': 'rub',
			'dest': '-1257786',
			'spp': '30',
			'nm': str(self.product_item),
		}

		return requests.get('https://card.wb.ru/cards/v2/detail', params=params, headers=headers)

	def product_data(self) -> dict | None:
		pass

	def product_image_url(self) -> str:
		pass
