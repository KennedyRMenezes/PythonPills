import requests
import os
import re

API_KEY = os.getenv("API_KEY")


def views_likes_dur(id):

    VIDEO_ID = id

    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={VIDEO_ID}&key={API_KEY}'

    reponse = requests.get(url)
    data = reponse.json()

    # Verificar e exibir os dados
    if 'items' in data and data['items']:
        video_info = data['items'][0]
        title = video_info['snippet']['title']
        description = video_info['snippet']['description']
        views = video_info['statistics']['viewCount']
        likes = video_info['statistics']['likeCount']

        dur = str(video_info["contentDetails"]["duration"])

        pattern = r'PT(?:(\d+)M)?(?:(\d+)S)?'
        dur = re.split(pattern, dur)
        sec = int(dur[2])
        if dur[1]:
            minu = int(dur[1])
            minu = minu * 60
            dur = minu + sec
        else:
            dur = sec
        
        # print("Título:", title)
        # print("Descrição:", description)
        # print("Visualizações:", views)
        # print("Curtidas:", likes)

        return views, likes, dur

    else:
        print("Vídeo não encontrado ou informações indisponíveis.")


