import tweepy
import os

import time

from click._compat import raw_input
from flask import session

auth=tweepy.OAuthHandler('t5qZhGyVwTkNArktAPM64nSvl','lk2ViVadYV6JbyeY7KLRfcDSxV9aGdn9ez9pTTO8cylnO7Z16J')
# auth.set_access_token('886710661014634498-n1ye6xnQzlGg4EWCX4FsjewnXmNodTA','BI5xGBqGVjxbRv2GTnUdi5JrUsmOcCahq740RjTqNE9sE')
print(auth.get_authorization_url())
# accesstoken=input("ACCT\n")s
# accesssecret=input("ACCS\n")
# auth.set_access_token(accesstoken,accesssecret)
# session.set('request_token', auth.request_token['oauth_token'])

token=auth.request_token['oauth_token']
verifier = raw_input('Verifier: ')

auth.request_token = { 'oauth_token' : token,
                         'oauth_token_secret' : verifier }



try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token.')

    key=auth.access_token
    secret=auth.access_token_secret

    auth.set_access_token(key, secret)


#
# token = session.get('request_token')
# session.delete('request_token')
# auth.request_token = { 'oauth_token' : token,
#                          'oauth_token_secret' : verifier }
#
# try:
#     auth.get_access_token(verifier)
# except tweepy.TweepError:
#     print('Error! Failed to get access token.')


api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user=api.me()

print(user.screen_name)
