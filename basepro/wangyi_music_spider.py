import json
import os
import time
import requests


'''
评论
初步希望可以拿到，歌词。。评论随意。。音乐，应该不容易的吧，试一下

同一首歌的encSecKey，params值是通用的

评论的url要镶嵌入歌曲id，而评论的url是死的，data加密参数有id，想要id应该是多爬取歌单，存入映照

https://music.163.com/#/song?id=272578    莫斯科没有眼泪


'''
headers={
'authority': 'music.163.com',
'method': 'POST',
'path': '/weapi/song/lyric?csrf_token=',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9'
}

