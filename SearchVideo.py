from youtube_transcript_api import YouTubeTranscriptApi
from contextlib import suppress
from itertools import chain
from googleapiclient.discovery import build
#from apiclient.errors import HttpError
from oauth2client.tools import argparser
import array as arr
import os
import nltk
import nltk.corpus
import numpy as np
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import pandas as pd
from nltk.corpus import stopwords

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


argparser.add_argument("--q", help="Search term", default="Fintech")
#argparser.add_argument("--trackKind", help="Search term", default="ASR")
#change the default to the search term you want to search
argparser.add_argument("--max-results", help="Max results", default=25)
#default number of results which are returned. It can vary from 0 - 100
args = argparser.parse_args()
options = args

#def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
  q=options.q,
  type="video",
  part="id,snippet",
  maxResults= 1,
  videoCaption= "closedCaption",
  eventType= "completed",
  #options.max_results



).execute()


videos = {}

# Add each result to the appropriate list, and then display the lists of
 # matching videos.
 # Filter out channels, and playlists.
for search_result in search_response.get("items", []):
  if search_result["id"]["kind"] == "youtube#video":
  #   for each_video in search_result["id"]["videoId"]:
       #idVideo = search_result["id"]["videoId"]
     #  print("Id6lapdypd1Bg")
      # print(YouTubeTranscriptApi.get_transcript("Id6lapdypd1Bg", languages=['en']))
 # videos.append("%s" % (search_result["id"]["videoId"]))
   videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"], \
                                           search_result["snippet"]["publishedAt"], \
                                           search_result["snippet"]["title"], \
                                           search_result["snippet"]["description"]

  #print ("Videos:\n", "\n".join(videos), "\n")

#with suppress(YouTubeTranscriptApi.CouldNotRetrieveTranscript):

FinalDict={}
for eac in videos.keys():
    eac
    vid_data = YouTubeTranscriptApi.get_transcript(eac, languages=['en'])
    #print(len(vid_data))
    #print(YouTubeTranscriptApi.get_transcript(eac, languages=['en']))
    if not isinstance(vid_data, type(None)) :
        #Parse the Array of Dictionary
        eachTextString=''
        fullTextString = ''
        videoKV ={}
        i =0
        while i < len(vid_data):
            eachTextString = ''.join(vid_data[i]['text'])
            fullTextString = fullTextString +" "+ eachTextString
            i+=1
        videoKV[eac]=fullTextString
        #print(videoKV)

        #text_file = open("C:\\Users/shiva/Desktop/Output.txt", "w")
        #text_file.write(videoKV.values())
        #text_file.close()

        textvalue = np.str(videoKV.values())

        # Cleaning of Text
        replace1 = textvalue.replace("[music]", "")
        replace2 = replace1.replace("[applause]", "")
        replace3 = replace2.replace("[", "")
        replace4 = replace3.replace("]", "")
        replace5 = replace4.replace('"', "")


        #textvalue = textvalue.apply(lambda x: " ".join(x.lower() for x in x.split()))
        #nltk.download('stopwords')
        #stop = stopwords.words('english')
        #textvalue =  textvalue.apply(lambda x: " ".join(x for x in x.split() if x not in stop))
        #print(textvalue)

# Text Mining

        #df = pd.DataFrame.from_dict({'videoid' : videoKV.keys(), 'text' : videoKV.values()})
        #df.head()
        #df.to_stringto_pickle("C:\\Users/shiva/Desktop/Output.txt")
        #print(df['text'])

#data = pd.read_csv(videoKV)
       # file2write = open("C:\\Users/shiva/Desktop/VideoData.txt", 'w')
        #file2write.write(str(videoKV))
        #file2write.close()
#corp = PlaintextCorpusReader("C:\\My Data/Data/Shiva/DWH/Hadoop", ".txt")

#text = nltk.Text(corp.words())
#match = text.concordance('hadoop')

#except: YouTubeTranscriptApi.CouldNotRetrieveTranscript


#print(videos)
   #listOfVideos = ','.join(videos.keys())

    #print(search_result)
