from loader import bot
import handlers  # noqa
from price_checker import PriceChecker

if __name__ == '__main__':
	PriceChecker().start()

	bot.infinity_polling()
