
from flask import Flask, request, render_template, jsonify
import json
from twitterAPI  import followPeople, create_friendship, create_favorite, retweet, get_tweets, reply_to_tweet
application = Flask(__name__)

@application.route('/find_tweets_by_phrase', methods=['POST'])
def getting_some_sweet_tweets():
    data = json.loads(request.data)
    return jsonify(get_tweets(data['phrase'], data['twitterCredentials']))

@application.route('/create_friendship', methods=['POST'])
def follow_new_friend():
    data = json.loads(request.data)
    return create_friendship(data['follower_id'], data['twitterCredentials'])

@application.route('/create_favorite', methods=['POST'])
def fav_a_tweet():
    data = json.loads(request.data)
    return create_favorite(data['tweet_id'], data['twitterCredentials'])

@application.route('/create_retweet', methods=['POST'])
def re_tweet():
    data = json.loads(request.data)
    return retweet(data['tweet_id'], data['twitterCredentials'])

@application.route('/reply_to_tweet', methods=['POST'])
def reply_tweet():
    data = json.loads(request.data)
    return reply_to_tweet(data['tweet_id'], data['status'], data['twitterCredentials'])

@application.route('/follow_random', methods=['POST'])
def follow_randos():
    data = json.loads(request.data)
    return jsonify(followPeople(thatSaid=data['thatSaid'], credentials= data['twitterCredentials'], atMost=data['atMost'], polarityMin=data['polarityMin']))

@application.route('/', methods=['GET'])
def index():
    return "Tweepy API for Hey Cindy!"

if __name__ == "__main__":
    application.debug = True
    application.run()