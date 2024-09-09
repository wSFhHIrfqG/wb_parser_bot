from threading import Thread
import time

from loader import bot
import parse
import database
import messages
from utils.get_price import get_price


class PriceChecker(Thread):

	def run(self):
		time.sleep(60 * 10)
		self.check_products()

	def check_products(self):
		for product in database.read.all_products():
			_id, chat_id, product_item, size_name, old_price = product

			product = parse.wb_product.WBProduct(product_item)
			product_data = product.product_data()

			actual_price = get_price(
				product_data.get('sizes'),
				size_name
			)

			product_card = messages.product_card.ProductCard(
				product_item=product_item, product_data=product_data, size_name=size_name
			)

			if self.product_stocked(old_price, actual_price):  # Товар появился в наличии
				msg = bot.send_photo(
					chat_id,
					product_card.image_link,
					product_card.caption(),
					parse_mode='html',
					reply_markup=product_card.markup()
				)
				bot.reply_to(
					msg,
					'🛒 Товар появился в наличии!'
				)
			elif self.price_decrease(old_price, actual_price):  # Цена на товар снизилась
				msg = bot.send_photo(
					chat_id,
					product_card.image_link,
					product_card.caption(),
					parse_mode='html',
					reply_markup=product_card.markup()
				)
				bot.reply_to(
					msg,
					'🛒 Цена на товар снизилась!'
					f'{old_price} ₽ ➡️ {actual_price} ₽'
				)

	@staticmethod
	def product_stocked(old_price: int | None, actual_price: int | None):
		"""Товар появился в наличии"""
		if (old_price is None) and (actual_price is not None):
			return True
		return False

	@staticmethod
	def price_decrease(old_price: int | None, actual_price: int | None):
		"""Цена на товар снизилась"""
		if (old_price is not None) and (actual_price is not None):
			if actual_price < old_price:
				return True
		return False
