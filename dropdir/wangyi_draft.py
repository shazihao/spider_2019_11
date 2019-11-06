'''
i

'''
import requests

'''

{"rid":"R_SO_4_478106252","offset":"20","total":"false","limit":"20","csrf_token":""}

010001

00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa
6d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46
bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7

0CoJUm6Qyw8W8jud

http://music.163.com/api/v1/resource/comments/R_SO_4_516997458?limit=20&offset=40    接口格式

https://music.163.com/#/song?id=272578    莫斯科没有眼泪     id=32408263    
KnqlE5vxkdpPlaCIilsVsOmM5KmMz8hXgW87MqAaU+Lt9qaMsMV95SrVCqEpGI2Hr7XjaJagr+LwPY8+Zsr+feRC9UfStmCZMQIYh5TGMuc=
3Wr5E6zXlDdhGHlfwxFFZBaQMJ6oajRkW4ghgjftSDaG4HSBUVoxB8T7uNq0SGuPyH/ZeNEOx0W6qdOz0iIzTpe2UJPz2Vc/e5zZanjnRb6HNz1lEECxwHo1WnsWiYzN
75968ab22bd3a3c951fa23f3565651bbe1e658224e3e51fce2439ee581c30a86c7b133ed0eb9ede372e1f5c28ff02f9ed8e025c6323261868ace3fcd3b467c63965e24dc882760ffb4c6b1ff992916d0fb9507bb051c2139fe11a4325489c8c7aeed9bc7d295153bb749a73bd10773f9ac207be1bdd17e7daedcda0abcfd83a0

5498a4368d5ae713322a350d66819605994af1be910eee693bee51d1f32bd5da89f5cd1dbcc198ad233cd8c9f2861a0acc2df8eac3cd202349fc3160043c33627acfb040ed7fb23e7f43179c6494c3f7f2170f59874bc9c18e36705b5520219d3e3dc5bd0930daf52670839ae1bba106bf14c010ea9807c8fbbd6083bf5128fe
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
url='https://music.163.com/weapi/song/lyric?csrf_token='

data={
'params': 'KnqlE5vxkdpPlaCIilsVsOmM5KmMz8hXgW87MqAaU+Lt9qaMsMV95SrVCqEpGI2Hr7XjaJagr+LwPY8+Zsr+feRC9UfStmCZMQIYh5TGMuc=',
'encSecKey': '75968ab22bd3a3c951fa23f3565651bbe1e658224e3e51fce2439ee581c30a86c7b133ed0eb9ede372e1f5c28ff02f9ed8e025c6323261868ace3fcd3b467c63965e24dc882760ffb4c6b1ff992916d0fb9507bb051c2139fe11a4325489c8c7aeed9bc7d295153bb749a73bd10773f9ac207be1bdd17e7daedcda0abcfd83a0'
}

response=requests.post(url=url,headers=headers,data=data).text

print(response)