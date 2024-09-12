def get_price(sizes: list, size_name: str):
	price = None
	for size in sizes:
		if size.get('name') == size_name:
			price = size.get('price', {}).get('total')
			break
	return price
