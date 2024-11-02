import requests
import os
from video_views_and_likes import views_likes_dur

API_KEY = os.getenv("API_KEY")
CHANNEL_ID = "---"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"


def get_all_videos(channel_id):

    videos = []

    url = f"{BASE_URL}?key={API_KEY}&channelId={channel_id}&part=snippet&type=video&order=date&maxResults=50"
    next_page_token = None
    
    while True:
        # Adiciona o token de página, se houver
        if next_page_token:
            full_url = f"{url}&pageToken={next_page_token}"
        else:
            full_url = url

        response = requests.get(full_url)
        data = response.json()


        # Adiciona os vídeos da página atual à lista
        for item in data.get("items", []):

            views, likes, _ = views_likes_dur(str(item["id"]["videoId"]))

            title = str(item["snippet"]["title"])
            title = title.strip()

            video_info = {
                "videoId": item["id"]["videoId"],
                "title": title,
                "publishedAt": item["snippet"]["publishedAt"],
                "views": views,
                "likes": likes
            }
            videos.append(video_info)

        # Verifica se há uma próxima página
        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break

    return videos

# Chama a função e imprime os vídeos
videos = get_all_videos(CHANNEL_ID)

print(f"\n{'Title'.ljust(50)} | {'Views'.ljust(15)} | {'Likes'.ljust(15)}\n")
print("="*80)
for video in videos:
    print(f"{video['title'].ljust(50)} | {video['views'].ljust(15)} | {video['likes'].ljust(15)}")
print()