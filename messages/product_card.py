import keyboards


class ProductCard:
	def __init__(self, product_item: int, product_data: dict, size_name: str | None = None):
		self.product_item = product_item
		self.product_data = product_data
		self.size_name = size_name
		self.sizes = product_data.get('sizes')
		self.image_link = product_data.get('image')

	def caption(self):
		if self.size_name is not None:
			caption_text = self._product_details_text() + self._product_price_part(size_name=self.size_name)
		else:
			caption_text = self._product_details_text()
		return caption_text

	def markup(self):
		if self.size_name is not None:
			reply_markup = keyboards.inline.add_product.add_product_markup(self.product_item, size_name=self.size_name)
		else:
			reply_markup = keyboards.inline.sizes.product_sizes_markup(self.product_item, self.sizes)
		return reply_markup

	def _product_details_text(self):
		text = f"" \
			   f"<b>Артикул:</b> {self.product_item}\n" \
			   f"<b>Название:</b> {self.product_data.get('name')}\n\n" \
			   f"<b>Бренд:</b> {self.product_data.get('brand')}<b>\n" \
			   f"Рейтинг:</b> {self.product_data.get('rating')}✮ " \
			   f"({self.product_data.get('feedbacks')} отз.)\n"
		return text

	def _product_price_part(self, size_name: str):
		price_info = None
		for size in self.sizes:
			if size.get('name') == size_name:
				price_info = size.get('price')
				break

		if price_info is None:
			text = '\n📦 <b>Нет в наличии</b>'
		else:
			text = f"\n<b>Цена:</b> " \
				   f"<s>{price_info.get('basic')} ₽</s> " \
				   f"{price_info.get('total')} ₽"
		return text
