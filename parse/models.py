from pydantic import BaseModel, Field, field_validator


class PriceBlock(BaseModel):
	basic: int = None
	total: int = None

	@field_validator('basic')
	@classmethod
	def convert_basic_price(cls, v: int):
		return v // 100

	@field_validator('total')
	@classmethod
	def convert_total_price(cls, v: int):
		return v // 100


class SizeBlock(BaseModel):
	name: str = Field(alias='origName')
	price: PriceBlock = None


class Product(BaseModel):
	name: str
	brand: str
	rating: float = Field(alias='reviewRating')
	feedbacks: int
	sizes: list[SizeBlock]
