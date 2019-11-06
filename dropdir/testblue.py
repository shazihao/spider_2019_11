import json
import os
import time
import requests

'''

16315为哆啦A梦S历险记特别篇的id
36076为第一卷，-36087第12卷


'''


def get_page(juan_id,time_stamp):
    url='http://v3api.dmzj.com/chapter/16315/{}.json?timestamp={}&channel=Android&_debug=0&version=2.7.019'.format(juan_id,time_stamp)
    headers={
    'User-Agent': 'Version/119   Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
    'Host': 'v3api.dmzj.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
    }
    response=requests.get(url=url,headers=headers).text
    response=json.loads(response)
    page_url=response['page_url']
    print('以获取到所需列表。。。')
    return page_url

def get_everypage(juan,list):
    page_count=1
    len_list=len(list)
    dir_name = r'../哆啦A梦七小子（s冒险篇）卷{}'.format(juan)
    if not os.path.isdir(dir_name):
        print('创建文件夹-哆啦A梦七小子（s冒险篇）卷{}-'.format(juan))
        os.makedirs(dir_name)

    for i in list:
        url=i
        headers = {
            'Referer': 'http://images.dmzj.com/',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10)',
            'Host': 'imgsmall.dmzj.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url=url, headers=headers)

        with open(r'../哆啦A梦七小子（s冒险篇）卷{}/哆啦A梦第{}页.jpg'.format(juan,page_count), 'wb') as f:
            print('正在加载--第{}页--/{}'.format(page_count,len_list))
            f.write(response.content)
            print('-第{}页-加载完毕')
            time.sleep(3)
        page_count+=1


if __name__ == '__main__':
    juan=int(input('请输入需要爬取的卷数，共十二卷:\n'))
    if juan<13 and juan>0:
        juan_id=str(juan+36075)
        time_stamp=int(time.time())
        list=get_page(juan_id,time_stamp)
        get_everypage(juan, list)
    else:
        print('大哥。。汉字啊，一共十二卷')