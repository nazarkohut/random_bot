"""Youtube channel ids parser"""
from utils.misc.parsers.html_parsers.functions import get_content

channel_list = ["https://www.youtube.com/@ThomasFlight", "https://www.youtube.com/@WarnerBrosPictures"]

channel_ids = list()
for ind, channel in enumerate(channel_list):
    content = get_content(channel)
    channel_id = content.find(itemprop="channelId").get('content')
    channel_ids.append(channel_id)

print(channel_ids)
