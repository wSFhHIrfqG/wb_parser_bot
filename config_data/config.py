import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
	exit('.env file not exists')
else:
	load_dotenv()

TOKEN = os.getenv('TOKEN')
