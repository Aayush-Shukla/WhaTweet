import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
DATABASE = os.getenv('DATABASE')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')