# enconding utf-8
import tweepy
from tweepy import API
from tweepy import OAuthHandler
import pandas as pd
import env


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

    def get_tweets(self, num_tweets, hash_tag_list):
        msg = []
        all_msgs = []
        api = self.twitter_client
        try:
            for hashtag in hash_tag_list:
                for tweet in tweepy.Cursor(api.search, q=hashtag, rpp=100).items(num_tweets):
                    msg = [tweet.user.screen_name, tweet.user.followers_count, hashtag, tweet.text, tweet.created_at]
                    all_msgs.append(msg)
            df = pd.DataFrame(all_msgs)
            df_result = df.sort_values(df[1])
            df_result = df_result.head(5)
            df_result.to_csv('RESULTS.csv', encoding='utf-8')
            return df_result
        except Exception:
            raise Exception


# # # # TWITTER AUTH # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(env.CONSUMER_KEY, env.CONSUMER_SECRET)
        auth.set_access_token(env.ACCESS_TOKEN, env.ACCESSS_TOKEN_SECRET)
        return auth


if __name__ == '__main__':

    hash_tag_list = [
        "#cloud",
        "#container",
        "#aws",
        "#devops",
        "#microservices",
        "#docker",
        "#openstack",
        "#automation",
        "#gcp",
        "#azure",
        "#istio",
        "#sre"]

    twitter_client = TwitterClient()
    twitter_client.get_tweets(100, hash_tag_list)
