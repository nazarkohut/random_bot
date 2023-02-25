from utils.misc.additional_functions.random_video.get_random_channel_id import get_channel_id
from aiogram import types
from loader import dp
from googleapiclient.discovery import build
import random
from config import GOOGLE_API_KEY

youtube = build("youtube", "v3", developerKey=GOOGLE_API_KEY)


@dp.message_handler(commands="random_youtube_video")
async def get_video(message: types.Message):

    channel_id = get_channel_id()

    channels_response = youtube.channels().list(
        id=channel_id,
        part="contentDetails"
    ).execute()

    playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    playlist_items = []
    next_page_token = None
    while True:
        playlist_items_response = youtube.playlistItems().list(
            playlistId=playlist_id,
            part="snippet",
            maxResults=2000,
            pageToken=next_page_token
        ).execute()
        playlist_items.extend(playlist_items_response["items"])
        next_page_token = playlist_items_response.get("nextPageToken")
        if not next_page_token:
            break

    random_video = random.choice(playlist_items)

    video_id = random_video["snippet"]["resourceId"]["videoId"]

    video_url = f"https://www.youtube.com/watch?v={video_id}"

    await message.answer(f"Video URL: {video_url}")
