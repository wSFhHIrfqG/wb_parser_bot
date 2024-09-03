import requests

import models


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
		response = self.__get_response()

		json_data = response.json()

		products = json_data.get('data').get('products')

		product_data = models.Product(**products[0]).dict()
		product_data['image'] = self.product_image_url()

		return product_data

	def product_image_url(self) -> str:
		vol = self.product_item // 100_000
		part = self.product_item // 1000

		if 0 <= vol <= 143:
			basket = '01'
		elif vol <= 287:
			basket = '02'
		elif vol <= 431:
			basket = '03'
		elif vol <= 719:
			basket = '04'
		elif vol <= 1007:
			basket = '05'
		elif vol <= 1061:
			basket = '06'
		elif vol <= 1115:
			basket = '07'
		elif vol <= 1169:
			basket = '08'
		elif vol <= 1313:
			basket = '09'
		elif vol <= 1601:
			basket = '10'
		elif vol <= 1655:
			basket = '11'
		elif vol <= 1919:
			basket = '12'
		elif vol <= 2045:
			basket = '13'
		elif vol <= 2189:
			basket = '14'
		elif vol <= 2405:
			basket = '15'
		elif vol <= 2621:
			basket = '16'
		else:
			basket = '17'

		src = f'https://basket-{basket}.wbbasket.ru/vol{vol}/part{part}/{self.product_item}/images/big/1.webp'
		return src
