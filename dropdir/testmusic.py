import base64
import sys

import sys
import time
from Crypto.Cipher import AES

# encrypt_text=b'\x97@\xd1yv\xf9h\x0b\xe2\x84D\x0353\x1bM\xae\xfe\x9c\xf3\xc67\xf1\xf4\xd2S\xaf\x13\xf8x\x0b\xb2[{\xcch40\x89\x0f\xb2x|\xc6\xfer\xbc\xdbe\xbb\xb5\xf4Y?\x89\xcaV\xf9\x17\xd0Ij\xaf\xc4'
# # a=encrypt_text
# # print(a)
# # encrypt_text = base64.b64encode(encrypt_text)
# # print(encrypt_text)
# # print(type(encrypt_text))
# # print('8888888'*6)
# # print(a)
# # print( bytes.decode(encrypt_text))



# a='沙子豪'
# b=a.encode('gbk')
# c=base64.b64encode(b)
# d=c.decode()
# print(a)
# print( b)
# print( c)
# print( d)
# print(b.decode('gbk'))
# print(bytes.decode(b))
# i=0
# for j in range(15):
#     zhi=chr(j)
#     while chr(i)==zhi:
#         print('{}相同{}'.format(i,j))
#         i+=1
#         if i>=50:
#             print('daole')
#             zhi='dfs'
# list1=list('1'+chr(0)+'1')
# list2=list('1'+chr(1)+'1')
# print(list1)
# print(list2)
# if list1==list2:
#     print('jjjj')
# if chr(0)==chr(1):
#     print('6666')
# print(15 % 16)

a='沙子豪'
vi='1122334455667788'.encode('utf-8')
text='JOJO这才是要加密的内容'.encode('utf-8')+b'\x03'#16倍数

secret_1=AES.new(a.encode('utf-8')+b'\x03'*7,AES.MODE_CBC,vi)
secret_2=AES.new(a.encode('utf-8')+b'\x03'*7,AES.MODE_CBC,vi)
secret_3=AES.new(a.encode('utf-8')+b'\x03'*7,AES.MODE_CBC,vi)

sec1=secret_1.encrypt(text)
sec2=secret_2.encrypt(text)
sec3=secret_3.encrypt(text)

print(sec1)
print(sec2)
print(sec3)

encrypt_text1 = base64.b64encode(sec1)
encrypt_text2 = base64.b64encode(sec2)
encrypt_text3 = base64.b64encode(sec3)


print(encrypt_text1)
print(encrypt_text1.decode())
print(encrypt_text2)
print(encrypt_text1.decode())
print(encrypt_text3)
print(encrypt_text1.decode())


# for i in secret_1.:
#     print(i)