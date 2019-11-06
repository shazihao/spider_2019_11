import os
import time
import requests
from lxml import etree
'''
要多写一层外面。缓一下，先处理app  ----》用一个爬虫处理了。


努努书坊似乎没有关于作品和作者查询的方法
eg:当年明月 作品集页面 www.kanunu8.com/files/writer/155.html

https://www.kanunu8.com/files/chinese/201102/1777.html  明一目录页码
77,78,66，79，80,67,81
https://www.kanunu8.com/files/chinese/201102/1781.html     7

异常没办法及时存入这个list
乱码问题，把返回的response进行操作
con=requests.get(url=url,headers=headers)
con.encoding='GBK'

&nbsp;   \xa0  那啥，就是前面的空格
\u3000  全角空白符

\r    反正list一下看看吧

'''



headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',

}

def get_content(url,fir_con):#返回内容,fir_con用于递归
    con=requests.get(url=url,headers=headers)
    con.encoding='GBK'
    con=con.text

    tree = etree.HTML(con)
    ori_con = tree.xpath('//div/table[5]//tr/td[2]/p/text()')



    for m_con in ori_con:
        m_con=m_con.replace(u'\xa0','')
        m_con=m_con.replace('\r','')
        fir_con+=m_con
    time.sleep(2)

    print(fir_con)
    time.sleep(20)
    # if urlnext!=unext and unext!='javascript:void(0)':#处理文本信息，有少数杂文，目前未装备删除
    #     get_content(url,urlnext,fir_con)
    # fir_con=fir_con.replace('  ','\n')
    return fir_con

def writer_con(cata,content):


    with open(r'../哑舍一/{}.txt'.format(cata), 'w',encoding='utf8') as f:
        f.write(content)


def spider_main():
    #有就读没有就创
    root_dir = r'../明朝那些事儿'
    root_catalogue=root_dir+'/a_catalogue.txt'

    if not os.path.exists(root_catalogue):

        os.makedirs(root_dir)
        open(root_catalogue,'w').close()
        fiddler_list=[]
    else:
        with open(root_catalogue,'r',encoding='utf8') as f:
            st=f.read()
            fiddler_list=st.split('\n')[:-1]#注意是否打了回车

    url_1 = 'www.kanunu8.com/files/writer/155.html'

    try:
        content=requests.get(url=url_1,headers=headers)
        content.encoding = 'GBK'
        content = content.text
        tree = etree.HTML(content)
        url_list=tree.xpath('//tr/td[2]/table[2]//tr/td[2]/a/@href')
        cata_list=tree.xpath('//tr/td[2]/table[2]//tr/td[2]/a[@href]//text()')#双斜，有个strong标签

        print(url_list[2])
        print('测试是否拿到东西')
        print(cata_list[0]+'\n')

        url_1='www.kanunu8.com'
        if len(url_list)==len(cata_list):
            #除最后一篇
            print(len(url_list))
            time.sleep(50)
            for i in range(len(url_list)):
                if url_list[i] not in fiddler_list:
                    url=url_1+url_list[i]

                    cata=cata_list[i]
                    print('{}加载开始'.format(cata))
                    fir_con=''
                    content=get_content(url,fir_con)
                    writer_con(cata, content)
                    print('{}加载完毕'.format(cata))
                    fiddler_list.append(url_list[i])
                    time.sleep(5)

        else:
            print('哈，算是异常了吧，url_list！=cata_list')

        url_1=0
        root_catalogue=r'../明朝那些事儿/a_catalogue.txt'
        if not os.path.isdir(root_catalogue):
            # print(root_catalogue)
            os.makedirs(root_catalogue)
        with open(root_catalogue,'w',encoding='utf8') as f:
            f_con=''
            for i in fiddler_list:
                f_con+=i+'\n'
            st=f.write(f_con)
    except Exception as err:
        if url_1:
            with open(r'../明朝那些事儿/a_catalogue.txt','w',encoding='utf8') as f:
                f_con = ''
                for i in fiddler_list:
                    f_con += i + '\n'
                st = f.write(f_con)
        print(err)
        print('走了异常')


if __name__ == '__main__':
    # for i in range(7):
    spider_main()

