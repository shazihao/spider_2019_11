import json
import time
import urllib

import requests

from urllib import parse

'''
京东爬虫
可以改page来增加需要的爬取量，291的具体意义不明目前不影响其他搜索

https://search-x.jd.com/Search?callback=jQuery4094994&area=1&enc=utf-8&keyword=笔记本&adType=7&page=1&ad_ids=291:19&xtest=new_search&_=1571727721293keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&adType=7&page=1&ad_ids=291%3A19&xtest=new_search&_=1571727721293

keyword=笔记本&adType=7&page=1&ad_ids=291:19&xtest=new_search&_=1571727721293
'''
url='https://search-x.jd.com/Search?callback=jQuery4094994&area=1&enc=utf-8&keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&adType=7&page=1&ad_ids=291%3A19&xtest=new_search&_=1571727721293'

oriurl='https://search-x.jd.com/Search?callback=jQuery4094994&area=1&enc=utf-8&keyword=笔记本&adType=7&page=1&ad_ids=291:19&xtest=new_search&_=1571727721293'
keyword=input('查询点')

data={
'keyword':keyword,
'adType':'7',
'page':'1',
'ad_ids':'291:19',
'xtest':'new_search',
'_':'1571727721293'
}

mkurl='https://search-x.jd.com/Search?callback=jQuery4094994&area=1&enc=utf-8&'+urllib.parse.urlencode(data)
print(mkurl)
print(url)
print(parse.unquote(url))

# time.sleep(50)

headers={
'Host': 'search-x.jd.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
'Accept': '*/*',
'Referer': 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&kw=%E7%AC%94%E8%AE%B0%E6%9C%AC',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'ipLoc-djd=1-72-2799-0; __jda=122270672.1571727719762387707609.1571727720.1571727720.1571727720.1; __jdb=122270672.1.1571727719762387707609|1.1571727720; __jdc=122270672; __jdv=122270672|direct|-|none|-|1571727719762; __jdu=1571727719762387707609; shshshfp=dced7d77b53a4a75a1c913797ec52250; shshshfpa=43745df4-6077-ac07-b49e-307a58b688a4-1571727720; shshshfpb=43745df4-6077-ac07-b49e-307a58b688a4-1571727720; shshshsID=ee42e40bf3135a83fa5666002659e8f3_1_1571727721115'

}


response=requests.get(url=mkurl,headers=headers).text.split('(',1)[-1].rsplit(')',1)[0]


# print(response)
res=json.loads(response)['291']

print(res)
print('###'*20)
print(res[0])
print(res[0]['pc_price'])
print(res[0]['ad_title'])
print(res[0]['color'])
print(len(res))









