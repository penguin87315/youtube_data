from pprint import pprint
import youtube_dl
import requests
from pprint import pprint
from datetime import datetime
import pandas as pd
import numpy as np

token = ['', 'EAAaBlBUOkNESQ', 'EAAaBlBUOkNHUQ', 'EAAaB1BUOkNKWUI', 'EAAaB1BUOkNNZ0I', 'EAAaB1BUOkNQb0I','EAAaB1BUOkNLd0M', 'EAAaB1BUOkNONEM', 'EAAaB1BUOkNKQUQ', 'EAAaB1BUOkNNSUQ']
YOUTUBE_API_KEY = "AIzaSyCXiQ2Bfw7J3tq11oBuEU5fz6GanTww-LM"
url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails,status&playlistId=PL02zpjjwMEjpfzltSpMoW4asLg6BYR84h&key=AIzaSyCXiQ2Bfw7J3tq11oBuEU5fz6GanTww-LM&maxResults=50&pageToken=' 

video_ids = []
for i in token:
    r = requests.get(url + i)
    data = r.json()
    for data_item in data['items']:
        video_ids.append(data_item['contentDetails']['videoId'])

dt = []
for i in video_ids:
    try:
        youtube_url = 'https://www.youtube.com/watch?v=' + str(i)
        video_info = {}
        with youtube_dl.YoutubeDL() as ydl:
             info = ydl.extract_info(youtube_url, download=False)
             # pprint(info)
             video_info['ID'] = info.get('id')
             video_info['標題'] = info.get('title')
             video_info['觀看次數'] = info.get('view_count')
             video_info['上傳日期'] = info.get('upload_date')
        mylist = video_info.items()
        mylist = list(mylist)
        dt += [mylist]
    except:
        pass
dd_df = pd.DataFrame(dt)
dd_df.to_csv('dqcs.csv')
print('ok')
