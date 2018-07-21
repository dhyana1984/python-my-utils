# -*- coding: utf-8 -*-
"""
将数字转换为三位逗号分隔的格式,例如将123456转换为123,456
"""

def commas(N):
    digits=str(N)
    assert(digits.isdigit())
    result=''
    while digits:
        digits,last3 = digits[:-3],digits[-3:]
        result = last3 + ',' +result if result else last3
    return result
    

commas(12345612131)

