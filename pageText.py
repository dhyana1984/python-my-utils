"""
通过参数分页显示文档，在shell调用时通过参数输入文档和每页的行数
"""

def more(text, numlines=15):
    lines = text.splitlines()               
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys                               
    more(open(sys.argv[1]).read(), 10)       
