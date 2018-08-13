"""
分页显示输入文本
"""

import sys

def getreply():
    """
    读取交互式用户回复键，即使stdin重定向到某个文件或者管道
    """
    if sys.stdin.isatty():                       # 判断是否控制台输入
        return input('?')                        # 读取输入数据
    else:
        if sys.platform[:3] == 'win':            # 如果stdin重定向
            import msvcrt                        # 不能用于询问用户
            msvcrt.putch(b'?')
            key = msvcrt.getche()                # 使用win控制台工具
            msvcrt.putch(b'\n')                  # getch() 不能回应键
            return key
        else:
            assert False, 'platform not supported'
            #linux?: open('/dev/tty').readline()[:-1]
            
def more(text, numlines=10):
    """
    page multiline string to stdout
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and getreply() not in [b'y', b'Y']: break

if __name__ == '__main__':                      
    if len(sys.argv) == 1:                     
        more(sys.stdin.read())                 
    else:
        more(open(sys.argv[1]).read())         
