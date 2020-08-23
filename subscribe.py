from apscheduler.schedulers.blocking import BlockingScheduler
from utils import *
import tweepy
from twilio.rest import Client
from app import user_data
import datetime

sched=BlockingScheduler()
@sched.scheduled_job('interval',seconds=120)
def retweeter():
    print("retweeter running")


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)


    users=user_data.query.all()
    for user in users:
        tags=user.subscribe.split()
        for tag in tags:
            for tweet in tweepy.Cursor(api.search, q='{} -filter:retweets'.format(tag), result_type='recent', rpp=100,tweet_mode='extended').items(3):
                print(tweet.user.screen_name,tweet.user.name)

                if tweet.created_at+datetime.timedelta(seconds=120)>datetime.datetime.utcnow()-datetime.timedelta(hours=5, minutes=30):
                    message = client.messages.create(
                        from_='whatsapp:+14155238886',
                        body="*{}* ({}):\n\n{}".format(tweet.user.screen_name,tweet.user.name,tweet.full_text),
                        to=user.phno
                    )

                    print(message)



sched.start()