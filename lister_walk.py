'''用os.walk生成文件树'''

import sys, os

def lister(root):                                           # 传入根目录
    for (thisdir, subshere, fileshere) in os.walk(root):    # 生成目录树
        print('[' + thisdir + ']')
        for fname in fileshere:                             # 遍历目录下的文件
            path = os.path.join(thisdir, fname)             # 生成文件名
            print(path)

if __name__ == '__main__':
    lister(sys.argv[1])                                     
