# coding:utf-8

'''
@author = super_fazai
@File    : safe_utils.py
@Time    : 2018/8/1 11:31
@connect : superonesfazai@gmail.com
'''

"""
安全相关
"""

__all__ = [
    'encrypt',              # 加密算法
    'decrypt',              # 解密算法
]

def encrypt(key, tmp_str):
    '''
    加密算法
    :param key: 配合加密的key
    :param tmp_str: 待加密的str
    :return:
    '''
    b = bytearray(str(tmp_str).encode("gbk"))
    n = len(b) # 求出 b 的字节数
    c = bytearray(n*2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码
        c[j] = c1
        c[j+1] = c2
        j = j+2

    return c.decode("gbk")

def decrypt(key, tmp_str):
    '''
    解密算法
    :param key: 配合解密的key
    :param tmp_str: 待解密密的str
    :return: '' 解码失败 | 'xxx' 成功
    '''
    c = bytearray(str(tmp_str).encode("gbk"))
    n = len(c) # 计算 b 的字节数
    if n % 2 != 0 :
        return ''

    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j+1]
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        b[i]= b1
    try:
        return b.decode("gbk")
    except:
        return ''