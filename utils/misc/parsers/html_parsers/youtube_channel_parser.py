"""Youtube channel ids parser"""
# import time
# import pymongo
# from utils.misc.parsers.html_parsers.functions import get_content
# from loader import db
# collection = db.videos

# channel_list = []

"""To fill channel_list with youtube channels urls"""
# with open('../data/channels_urls.txt', 'r') as f:
#     for line in f:
#         channel_list.append(line.strip())
#
# print(channel_list)

"""To get youtube channel id and add them to list"""
# channel_ids = list()
# for ind, channel in enumerate(channel_list):
#     content = get_content(channel)
#     channel_id = content.find(itemprop="channelId").get('content')
#     channel_ids.append(channel_id)
#     print(ind, channel_id)


"""To append id to list(Use when abortion error, error can happen if you have more than 50 youtube channels urls"""
# with open('../data/channels_ids.txt', 'r') as f:
#     for line in f:
#         channel_ids.append(line.strip())
#
# print(channel_ids)
#
# """Add data to mongoDB"""
# for id in channel_ids:
#     collection.insert_one({"yt_id": id})
#
# print("finished")
