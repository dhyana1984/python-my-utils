# -*- coding: utf-8 -*-
"""
将数字转换为钱币格式，例如123456.967转换为123,456.97
"""

#将数字转换为3位逗号格式
def commas(N):
    digits=str(N)
    assert(digits.isdigit())
    result=''
    while digits:
        digits,last3 = digits[:-3],digits[-3:]
        result = last3 + ',' +result if result else last3
    return result
    



def money(N, width=0):
    flag = '-' if N<0 else ''
    N=abs(N)
    total = commas(int(N))
    fract = ('%.2f'%N)[-2:]
    formatting = '%s%s.%s'%(flag,total,fract)
    return '%*s'%(width,formatting)

