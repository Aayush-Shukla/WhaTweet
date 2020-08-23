import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
DATABASE = os.environ.get('DATABASE_URL')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
ACCOUNT_SID = os.environ.get('account_sid')
AUTH_TOKEN = os.environ.get('auth_token')