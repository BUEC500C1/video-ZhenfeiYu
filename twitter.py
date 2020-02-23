import tweepy
import os
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)   
api = tweepy.API(auth)

def get_tweets(foldername,searchword):
    folder = os.path.exists('../'+foldername+'/'+foldername+'_images')
    if not folder:                   
        os.makedirs('../'+foldername+'/'+foldername+'_images')           
        print ("Building new folder...")
    else:
        print ("This folder exits!")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []
    oldest = -1
    while len(alltweets) < 5:   
        new_tweets = api.search(q = searchword,count = 10,max_id = str(oldest),lan='en',include_entities = False)
        alltweets.extend(new_tweets)
        oldest = new_tweets[-1].id-1
        if(not new_tweets):
            break
    print("%s tweets found." % (len(alltweets)))   
    
    list_word = []
    x = '../'+foldername+'/'+foldername+".txt"
    f = open(x,"a+")
    for j in alltweets:
        list_word.append(j.text)
        print(j.text, "\n", file = f)
    f.close()
    return list_word

# if __name__ == '__main__':
#     foldername = input('Enter your foldername: ')
#     searchword = input('Enter the searchword you would like to search: ')
#     get_tweets(foldername,searchword)