# -*- coding: utf-8 -*-

import string
from csv import writer
import json
import os.path

#Number of txt parts
parts = 6

#keywords used for filter
keywords = [
            "midlothian", "dfwflood", "collapse", "padera" , "caldwell", "hays" , "san marcos",
            "wimberley", "#texasflood2015", "#severewx", "#severeflood", "#houstonflood",
            "#txwx", "#dfwwx", "#txflood", "#midlothiantx", "#texasflooding"
            ]

#blockedwords used for filter
blockedwords = [
                "avengers", "age of ultron", "tony stark", "hot seller", "chargers", "how hiring", "job", 
                "mother's day", "labor", "wedding", "bridal party", "star wars", "austin city limits", "33 days to digifest"
                ]

limitCatch = "{\"limit\":{\"track\":" #Catches "limit" text and ignores it

for d in range(27, 32):
    
    #Date written in month_day format
    date = "05_" + str(d)
    
    #Output data to CSV
    outFile = "tweets_wordfiltered_" + date + ".csv"
    out = open("tweets_wordfiltered/" + outFile, 'w')
    
    csv = writer(out)
    print >> out, 'tweetID, text, tweetTime, userID, userName, timeZone, lat, lon, tweetLoc, locType'
    
    for i in range(parts):
        tweets = []
        
        fileName = "data/tweets_" + date + "_Part" + str(i + 1) + ".txt"
        if not os.path.isfile(fileName):
            continue
        for line in open(fileName):
            try:
                if limitCatch not in line:
                    tweets.append(json.loads(line))
            except:
                pass

        #Organize data from tweets

        tweetID = [tweet['id_str'] for tweet in tweets] #tweet id
        text = [tweet['text'] for tweet in tweets] #text of tweet
        tweetTime = [tweet['created_at'] for tweet in tweets] #creation time of tweet

        userID = [tweet['user']['id_str'] for tweet in tweets] #user id
        userName = [tweet['user']['screen_name'] for tweet in tweets] #user name
        timeZone = [tweet['user']['time_zone'] for tweet in tweets] #time zone used

        lat = [(tweet['geo']['coordinates'][0] if tweet['geo'] else None) for tweet in tweets] #latitude tweet was posted
        lon = [(tweet['geo']['coordinates'][1] if tweet['geo'] else None) for tweet in tweets] #longitude tweet was posted

        tweetLoc = [(tweet['place']['full_name'] if tweet['place'] else None) for tweet in tweets] #location where tweet was posted can be a city or even a specific building
        locType = [(tweet['place']['place_type'] if tweet['place'] else None) for tweet in tweets] #the type of location

        rows = zip(tweetID, text, tweetTime, userID, userName, timeZone, lat, lon, tweetLoc, locType)

        for row in rows:
            values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
            
            for word in keywords:
                #This is the primary filter, in this example we make sure the tweet contains at least
                #one word from the keywords list and it must also have a latitude value
                if word in values[1].lower() and values[6] is not None:
                    #This is the primary filter, in this example we make sure the tweet does not contain 
                    #any word from the blocked words list
                    blockedwordfound = False
                    for blockedword in blockedwords:
                        if blockedword in values[1].lower():
                            blockedwordfound = True
                            break

                    if blockedwordfound == False:
                        values[0] = values[0] + "\t"
                        values[1] = values[1].replace("\t", " ")
                        values[1] = values[1].replace("\n", " ")
                        values[2] = values[2][0:19] + values[2][25:]
                        values[3] = values[3] + "\t"
                        csv.writerow(values)
                        break

    out.close()
