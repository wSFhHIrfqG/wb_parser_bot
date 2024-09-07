import unittest
from unittest import TestCase
from unittest.mock import MagicMock, patch

import price_checker


class TestCheckProducts(TestCase):
	def setUp(self) -> None:
		self.price_checker = price_checker.PriceChecker()

	def test_product_stocked(self):
		"""Товар появился в наличии"""
		product_data = {
			'id': 1,
			'chat_id': 1234,
			'product_item': 195466668,
			'size': '10',
			'price': None,
		}

		all_products = [
			product_data.values(),
		]

		actual_product_data = {
			"name": "Кроссовки, 574",
			"brand": "New balance",
			"rating": 4.5,
			"feedbacks": 24,
			"sizes": [
				{
					"name": "10",
					"price": {
						"total": 10_000
					}
				}
			],
			"image": "https://basket-13.wbbasket.ru/vol1954/part195466/195466668/images/big/1.webp"
		}

		with patch(
				'price_checker.database.read.all_products',
				return_value=all_products
		):
			with patch(
					'price_checker.parse.wb_product.WBProduct.product_data',
					return_value=actual_product_data):
				with patch(
						'price_checker.messages.product_card.ProductCard'):
					send_message_mock = MagicMock()
					price_checker.bot.send_message = send_message_mock

					reply_to_mock = MagicMock()
					price_checker.bot.reply_to = reply_to_mock

					self.price_checker.check_products()

					send_message_mock.assert_called_once()
					reply_to_mock.assert_called_once()

	def test_price_decrease(self):
		"""Цена на товар снизилась"""
		product_data = {
			'id': 1,
			'chat_id': 1234,
			'product_item': 195466668,
			'size': '10',
			'price': 10_000
		}

		all_products = [
			product_data.values(),
		]

		actual_product_data = {
			"name": "Кроссовки, 574",
			"brand": "New balance",
			"rating": 4.5,
			"feedbacks": 24,
			"sizes": [
				{
					"name": "10",
					"price": {
						"total": 9000
					}
				}
			],
			"image": "https://basket-13.wbbasket.ru/vol1954/part195466/195466668/images/big/1.webp"
		}

		with patch(
				'price_checker.database.read.all_products',
				return_value=all_products):
			with patch(
					'price_checker.parse.wb_product.WBProduct.product_data',
					return_value=actual_product_data):
				send_message_mock = MagicMock()
				price_checker.bot.send_message = send_message_mock

				reply_to_mock = MagicMock()
				price_checker.bot.reply_to = reply_to_mock

				self.price_checker.check_products()

				send_message_mock.assert_called_once()
				reply_to_mock.assert_called_once()

	def test_no_change(self):
		"""Статус товара никак не изменился; цена не упала"""
		product_data = {
			'id': 1,
			'chat_id': 1234,
			'product_item': 195466668,
			'size': '10',
			'price': 10_000
		}

		all_products = [
			product_data.values(),
		]

		actual_product_data = {
			"name": "Кроссовки, 574",
			"brand": "New balance",
			"rating": 4.5,
			"feedbacks": 24,
			"sizes": [
				{
					"name": "10",
					"price": {
						"total": 10_000
					}
				}
			],
			"image": "https://basket-13.wbbasket.ru/vol1954/part195466/195466668/images/big/1.webp"
		}

		with patch(
				'price_checker.database.read.all_products',
				return_value=all_products):
			with patch(
					'price_checker.parse.wb_product.WBProduct.product_data',
					return_value=actual_product_data):
				send_message_mock = MagicMock()
				price_checker.bot.send_message = send_message_mock

				reply_to_mock = MagicMock()
				price_checker.bot.reply_to = reply_to_mock

				self.price_checker.check_products()

				send_message_mock.assert_not_called()
				reply_to_mock.assert_not_called()


class TestStaticFunctions(TestCase):
	def setUp(self) -> None:
		self.price_checker = price_checker.PriceChecker()

	def test_product_stocked(self):
		# Товар пока не появился в наличии
		self.assertFalse(
			self.price_checker.product_stocked(
				old_price=None, actual_price=None)
		)

		# Товар появился в наличии
		self.assertTrue(
			self.price_checker.product_stocked(
				old_price=None, actual_price=100)
		)

		# Товара больше нет в наличии
		self.assertFalse(
			self.price_checker.product_stocked(
				old_price=100, actual_price=None)
		)

		# Цена повысилась
		self.assertFalse(
			self.price_checker.product_stocked(
				old_price=100, actual_price=200)
		)

		# Цена снизилась
		self.assertFalse(
			self.price_checker.product_stocked(
				old_price=200, actual_price=100)
		)

		# Цена не изменилась
		self.assertFalse(
			self.price_checker.product_stocked(
				old_price=100, actual_price=100)
		)

	def test_price_decrease(self):
		# Товар пока не появился в наличии
		self.assertFalse(
			self.price_checker.price_decrease(
				old_price=None, actual_price=None)
		)

		# Товар появился в наличии
		self.assertFalse(
			self.price_checker.price_decrease(
				old_price=None, actual_price=100)
		)

		# Товара больше нет в наличии
		self.assertFalse(
			self.price_checker.price_decrease(
				old_price=100, actual_price=None)
		)

		# Цена повысилась
		self.assertFalse(
			self.price_checker.price_decrease(
				old_price=100, actual_price=200)
		)

		# Цена снизилась
		self.assertTrue(
			self.price_checker.price_decrease(
				old_price=200, actual_price=100)
		)

		# Цена не изменилась
		self.assertFalse(
			self.price_checker.price_decrease(
				old_price=100, actual_price=100)
		)


if __name__ == '__main__':
	unittest.main()
