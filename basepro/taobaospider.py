import requests

from urllib import parse
'''
https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3D%25E7%25AC%2594%25E8%25AE%25B0%25E6%259C%25AC%26imgfile%3D%26commend%3Dall%26ssid%3Ds5-e%26search_type%3Ditem%26sourceId%3Dtb.index%26spm%3Da21bo.1000386.201856-taobao-item.1%26ie%3Dutf8%26initiative_id%3Dtbindexz_20170306'


https://login.taobao.com/member/login.jhtml?redirectURL=http://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.1000386.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306

'''

url='https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3D%25E7%25AC%2594%25E8%25AE%25B0%25E6%259C%25AC%26imgfile%3D%26commend%3Dall%26ssid%3Ds5-e%26search_type%3Ditem%26sourceId%3Dtb.index%26spm%3Da21bo.1000386.201856-taobao-item.1%26ie%3Dutf8%26initiative_id%3Dtbindexz_20170306'


# a=urllib.parse.quote
deco=parse.unquote(url)

print(deco)