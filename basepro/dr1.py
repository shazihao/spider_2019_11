import sys
import time

from Crypto.Cipher import AES
import base64
import requests
import json

'''
完整版网易云spider的草稿：

内置函数chr()返回对应数字的ASCII码对应，字节流：b'\x03\x03\x03'，为chr(3)的返回值
     text才是加密的内容！！！encode之后要补成16的倍数。

使用函数AES.new(伪加密对象，加密模式，vi)  执行完返回：   加密对象要补成16位
<Crypto.Cipher._mode_cbc.CbcMode object at 0x000001EFA46A50B8>
<class 'Crypto.Cipher._mode_cbc.CbcMode'>

之后可以执行encrypt(text)方法，参数为      执行完返回     
b'\x97@\xd1yv\xf9h\x0b\xe2\x84D\x0353\x1bM\xae\xfe\x9c\xf3\xc67\xf1\xf4\xd2S\xaf\x13\xf8x\x0b\xb2[{\xcch40\x89\x0f\xb2x|\xc6\xfer\xbc\xdbe\xbb\xb5\xf4Y?\x89\xcaV\xf9\x17\xd0Ij\xaf\xc4'
<class 'bytes'>

         base64.b64encode(b)是将b进行再一次的字节流加密  b'\xc9\xb3\xd7\xd3\xba\xc0' ==》 b'ybPX07rA'
之后执行base64.b64encode(encrypt_text)，参数为bytes字节流 执行完返回
b'l0DReXb5aAvihEQDNTMbTa7+nPPGN/H00lOvE/h4C7Jbe8xoNDCJD7J4fMb+crzbZbu19Fk/icpW+RfQSWqvxA=='
<class 'bytes'> 
.decode()把字节流取消掉，然后return


'''
headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/'
}
first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud".encode('utf-8')


def get_params():
    iv = "0102030405060708".encode('utf-8')
    first_key = forth_param
    second_key = 16 * 'F'.encode('utf-8')
    h_encText = AES_encrypt(first_param.encode('utf-8'), first_key, iv)
    h_encText = AES_encrypt(h_encText.encode('utf-8'), second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    # text.encode('utf-8')#補充
    pad = 16 - len(text) % 16#查余数
    text = text + pad * chr(pad).encode('utf-8')#chr()返回对应数字的ASCII码对应，字节流：b'\x03\x03\x03'，为chr(3)的返回值
    # print('这里是text \n')
    # print(text)
    # print( pad * chr(pad).encode('utf-8'))
    # print( pad * chr(pad))
    # print(text.decode())
    encryptor = AES.new(key, AES.MODE_CBC, iv)#形成对象
    # print(encryptor)
    # print(type(encryptor))
    encrypt_text = encryptor.encrypt(text)#加密，目前字节流
    # print(encrypt_text)
    # print(type(encrypt_text))
    encrypt_text = base64.b64encode(encrypt_text)#加密，目前字节流
    # print(encrypt_text)
    # print(type(encrypt_text))
    # print(encrypt_text.decode())
    # sys.exit(0)
    return encrypt_text.decode()#加密，解除字节流


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


if __name__ == "__main__":
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009/?csrf_token="
    params = get_params()
    encSecKey = get_encSecKey()
    json_text = get_json(url, params, encSecKey)
    json_dict = json.loads(json_text)
    time.sleep(5)
    for item in json_dict['comments']:
        # print(item['content'].encode('gbk', 'ignore'))
        # print(item['content'].encode('gbk')) #用于pycrypto    这里用的是pycryptodemo
        print(item['content'])
