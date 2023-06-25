from flask import Flask
import tweepy
import requests
from . import keys
  
# calling the twitter api 
api = tweepy.Client(bearer_token=keys.bearer, consumer_key=keys.consumer_key, consumer_secret=keys.consumer_secret, access_token=keys.access_token, access_token_secret=keys.access_token_secret)

app = Flask(__name__)

@app.route('/')
def home():
    category = 'life'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': keys.API_KEY})
    
    if response.status_code == requests.codes.ok:
        # posting the tweet
        data = response.json()
        quote = data[0]['quote']
        author = data[0]['author']
        tweet = f'"{quote}" - {author}'
        api.create_tweet(text=tweet)
        print("Tweeted Success!")
        return tweet

if __name__ == '__main__':
    app.run(debug=True)
