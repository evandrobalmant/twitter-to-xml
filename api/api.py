# -*- coding: utf-8 -*- 
import tweepy
from configuracao.models import Twitter as Config_twitter

class Twitter(object):
    
    def __init__(self): 
        
        self.twitter = Config_twitter.objects.all()
        
    
    def enviaTweet(self, descricao):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.update_status(descricao)
            
    def criarAmigo(self, usuario):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.create_friendship(usuario)
            
    def enviaMensagemDireta(self, usuario, texto):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.send_direct_message(user=usuario, text=texto)

    def getRetweets(self, limite = None):
        
        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            return tweepy.Cursor(api.retweets_of_me).items(limite)
    
    def getBusca(self, termo):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)

        return api.search(termo, rpp=25, lang='pt')
    
    def getMencoes(self, limite = None):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            
            return tweepy.Cursor(api.mentions).items(limite)
          
    def getHomeTimeline(self, limite = None):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            
            return tweepy.Cursor(api.user_timeline).items(limite)
