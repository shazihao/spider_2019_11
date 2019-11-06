import time
import requests
from lxml import etree
'''
最后那个是空列表要完善，给一个大的list，前半应该已经解决.....而且，异常没办法及时存入这个list

为什么没有第200章 不是没有，是在下面因为标题的不同，已处理


'''

headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def get_content(url,urlnext,fir_con):#返回内容
    con=requests.get(url=url,headers=headers).text
    tree = etree.HTML(con)

    ori_con=tree.xpath('//*[@id="chaptercontent"]/p/text()')
    for m_con in ori_con:
        fir_con+=m_con
    unext=tree.xpath('//*[@id="wrapbig"]/div/div[@class="nextPageBox"]/a[@class="next"]/@href')[0]
    time.sleep(2)

    if urlnext!=unext and unext!='javascript:void(0)':#处理文本信息，有少数杂文，目前未装备删除
        get_content(url,urlnext,fir_con)
    fir_con=fir_con.replace('  ','\n')
    return fir_con

def writer_con(cata,content):
    with open(r'../龙族五悼亡者的归来/{}.txt'.format(cata), 'w',encoding='utf8') as f:
        f.write(content)


with open(r'../龙族五悼亡者的归来/a_catalogue.txt','r',encoding='utf8') as f:
    st=f.read()
    fiddler_list=st.split('\n')[:-1]#注意是否打了回车


url_1 = 'https://www.35xs.org/book/300999/'

try:
    content=requests.get(url=url_1,headers=headers).text
    tree = etree.HTML(content)
    url_list=tree.xpath('//div/ul[@class="mulu_list"]/li/a/@href')
    cata_list=tree.xpath('//div/ul[@class="mulu_list"]/li/a/text()')

    print(url_list[4])
    print('测试是否拿到东西')
    print(cata_list[4]+'\n')

    if len(url_list)==len(cata_list):
        #除最后一篇
        for i in range(len(url_list)-1):
            if url_list[i] not in fiddler_list:
                url='https://www.35xs.org'+url_list[i]
                cata=cata_list[i].replace('龙族5悼亡者的归来  ','')
                print('{}加载开始'.format(cata))
                urlnext=url_list[i+1].rsplit('/',1)[-1]
                fir_con=''
                content=get_content(url, urlnext,fir_con)
                writer_con(cata, content)
                print('{}加载完毕'.format(cata))
                fiddler_list.append(url_list[i])
                time.sleep(5)
            #下面兩行沒啥用
            # else:
            #     print('{}链接已经存在'.format(url_list[i]))
        #最后一篇
        if url_list[-1] not in fiddler_list:
            url = 'https://www.35xs.org' + url_list[-1]
            cata = cata_list[-1].replace('龙族5悼亡者的归来  ','')
            print('{}加载开始'.format(cata))
            urlnext = '不会一样的'
            fir_con = ''
            content = get_content(url, urlnext, fir_con)
            writer_con(cata, content)
            print('{}加载完毕'.format(cata))
            fiddler_list.append(url_list[-1])
            time.sleep(5)
        else:
            print('最后一篇：{}链接已经存在'.format(url_list[-1]) + '\n没有更新。')

    else:
        print('哈，算是异常了吧，url_list！=cata_list')

    url_1=0
    with open(r'../龙族五悼亡者的归来/a_catalogue.txt','w',encoding='utf8') as f:
        f_con=''
        for i in fiddler_list:
            f_con+=i+'\n'
        st=f.write(f_con)
except Exception as err:
    if url_1:
        with open(r'../龙族五悼亡者的归来/a_catalogue.txt','w',encoding='utf8') as f:
            f_con = ''
            for i in fiddler_list:
                f_con += i + '\n'
            st = f.write(f_con)
    print('走了异常')
