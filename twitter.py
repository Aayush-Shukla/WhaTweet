import tweepy
import os

import time

from click._compat import raw_input
from flask import session

auth=tweepy.OAuthHandler('t5qZhGyVwTkNArktAPM64nSvl','lk2ViVadYV6JbyeY7KLRfcDSxV9aGdn9ez9pTTO8cylnO7Z16J')
auth.set_access_token('886710661014634498-n1ye6xnQzlGg4EWCX4FsjewnXmNodTA','BI5xGBqGVjxbRv2GTnUdi5JrUsmOcCahq740RjTqNE9sE')


"""Respond to incoming calls with a simple text message."""
# Fetch the message
# global init
# if init==0:
#     # session['phone_no']=request.form.get('From')
#     init=1

token=''
# num=0
lvl=0
ver=0
counter=0
login=0
init=0
sublvl=0
confirm=0
# resp = MessagingResponse()
# print("{}{}{}{}{}{}".format(num,ver,counter,login,init,session['phone_no'



"""0 - hello, 1 - verifier code, 2 - options, 3- make tweets ,4- show tweets"""

# while(1):
#     msg = input()
#
#     if lvl==4:
#
#         if(sublvl==1):
#             tweet=[]
#             if(len(msg)<280):
#                 tweet.append(msg)
#             else:
#                 count=0
#                 letter=0
#                 tweetno=len(msg)/280
#                 tweetno=(len(msg)+2*tweetno)//280
#                 tweetno=int(tweetno)
#
#                 while(letter<len(msg)):
#                     # print(msg[letter:letter+274])
#                     tweet.append(msg[letter:letter+274]+" ({}/{})".format(count+1,tweetno+1))
#                     count+=1
#                     letter=letter+275
#                     # tweet[count]+=" ({}/{})".format(count+1,tweetno+1)
#
#
#             print("You're going to make this/these tweet(s)\n------------------")
#             for i in tweet:
#                 print(i)
#                 sublvl=2
#         if(sublvl==2):
#             if(confirm==0):
#                 print("are you sure ? (y/n)?")
#                 confirm=1
#             else:
#                 if(msg=='y'):
#                     for i in tweet:
#
#                         api.update_status(i)
#                     print("done")
#                     sublvl=0
#                     confirm=0
#                     lvl=3
#
#
#
#
#
#
#
#
#         if(msg=='1' and sublvl==0):
#             print("Type your tweet in (LIMIT : 1000 words)")
#             sublvl=1
#
#         if(msg=='2' and sublvl==0):
#             trending=api.trends_place(23424848)
#
#             for i in range(10):
#                 print(i+1,trending[0]['trends'][i]['name'],trending[0]['trends'][i]['tweet_volume'])
#                 # print(trending[0]['trends'][i])
#             sublvl = 0
#             confirm = 0
#             lvl = 3
#
#         if(msg=='3' and sublvl==0):
#             print(api.get_direct_message())
#             sublvl = 0
#             confirm = 0
#             lvl = 3
#
#
#
#
#
#
#
#
#
#     if lvl==3:
#         api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#         user = api.me()
#         print("yo, {} ({})\n--------------\n What would you like to do? \n 1. Make Tweet\n 2. Trending".format(user.name,user.screen_name))
#         lvl=4
#
#
#     if lvl==2:
#         auth.request_token = {'oauth_token': token,
#                               'oauth_token_secret': verifier}
#         try:
#             auth.get_access_token(verifier)
#             lvl=3
#
#         except tweepy.TweepError:
#             print('Error! Failed to get access token.')
#             # lvl=0
#             # lvl=0
#             # ver=0
#             # counter=0
#             # login=0
#
#             # print("login:".format(login))
#
#         key = auth.access_token
#         secret = auth.access_token_secret
#
#         auth.set_access_token(key, secret)
#
#
#
#     if lvl==1:
#         token = auth.request_token['oauth_token']
#
#         verifier = msg
#
#
#         # ver=1
#         lvl=2
#
#
#
#
#     if lvl==0:
#         # if counter==0:
#         print("Hi there. Login to Twitter here. {} And send the code".format(auth.get_authorization_url()))
#             # counter=1
#         lvl=1
        # print("{}".format(counter))






    # start= print("Hi, {} ({})\n What would you like to do?\n1. Make Tweet\n".format(user.name,user.screen_name))
    # start.media("https://twitter.com/{}/photo".format(user.screen_name))


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
print(user)








































# print(auth.get_authorization_url())
# accesstoken=input("ACCT\n")s
# accesssecret=input("ACCS\n")
# auth.set_access_token(accesstoken,accesssecret)
# session.set('request_token', auth.request_token['oauth_token'])

# token=auth.request_token['oauth_token']
# verifier = raw_input('Verifier: ')
#
# auth.request_token = { 'oauth_token' : token,
#                          'oauth_token_secret' : verifier }
#
#
#
# try:
#     auth.get_access_token(verifier)
# except tweepy.TweepError:
#     print('Error! Failed to get access token.')
#
#     key=auth.access_token
#     secret=auth.access_token_secret
#
#     auth.set_access_token(key, secret)


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

#
# api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
# user=api.me()
#
# print(user.screen_name,user)
