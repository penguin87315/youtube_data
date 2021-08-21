from pprint import pprint
import youtube_dl
import requests
from pprint import pprint
from datetime import datetime
import pandas as pd
import numpy as np

token = []
YOUTUBE_API_KEY = "AIzaSyCXiQ2Bfw7J3tq11oBuEU5fz6GanTww-LM"
url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails,status&playlistId=PLE6ICy7YAcNYb3nFcr2ULAjiwHxwjaU0U&key=AIzaSyCXiQ2Bfw7J3tq11oBuEU5fz6GanTww-LM&maxResults=50&pageToken=' 
r = requests.get(url)
data = r.json()
next_page_token = data.get('nextPageToken', '')
token.append(next_page_token)

for i in token:
    r = requests.get(url + str(i))
    dts = r.json()
    npt = dts.get('nextPageToken', '')
token.append(npt)
ls = ['EAAaB1BUOkNKWUI', 'EAAaB1BUOkNNZ0I', 'EAAaB1BUOkNQb0I', 'EAAaB1BUOkNQb0I']
new = token + ls
new.insert(0,'')

video_ids = []
for i in new:
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
dd_df.to_csv('tzjn.csv')
print('ok')
