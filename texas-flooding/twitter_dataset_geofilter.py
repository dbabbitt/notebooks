# -*- coding: utf-8 -*-

import string
from csv import writer
import json

#Number of txt parts
parts = 7

#Date written in month_day format
date = "05_06"

#boundingboxes used for filter.  Item Format: {'SW-LAT' : 36, 'SW-LON' : -120, 'NE-LAT' : 42, 'NE-LON' : -110}
boundingboxes = [ {'SW-LAT' : 25.631673999999997, 'SW-LON' : -107.329864, 
                   'NE-LAT' : 36.622840000000004, 'NE-LON' : -88.866903}
                ]

limitCatch = "{\"limit\":{\"track\":" #Catchs "limit" text and ignores it

#Output data to CSV
outFile = "tweets_geofiltered_" + date + ".csv"
out = open("../tweets_geofiltered/" + outFile, 'w')

csv = writer(out)
print >> out, 'tweetID, text, tweetTime, userID, userName, timeZone, lat, lon, tweetLoc, locType'

for i in range(parts):
    tweets = []
    
    fileName = "../data/tweets_" + date + "_Part" + str(i + 1) + ".txt"
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
        
        for box in boundingboxes:
            #This is your geo filter, in this example we make sure the tweet location is 
            #within at least one of the bounding boxes.
            if box['SW-LAT'] <= values[6] and values[6] <= box['NE-LAT'] and box['SW-LON'] <= values[7] and values[7] <= box['NE-LON']:
                values[0] = values[0] + "\t"
                values[1] = values[1].replace(".", "")
                values[1] = values[1].replace("?", "")
                values[1] = values[1].replace("!", "")
                values[1] = values[1].replace(",", "")
                values[1] = values[1].replace("\t", "")
                values[1] = values[1].replace("\n", "")
                values[2] = values[2][0:19] + values[2][25:]
                values[3] = values[3] + "\t"
                csv.writerow(values)
                break

out.close()
