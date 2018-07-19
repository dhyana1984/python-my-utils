# -*- coding: utf-8 -*-
"""
计时器工具-测试函数性能
1.根据运行平台决定用time.clock还是time.time, windows对time.clock精度比较高
2.允许重复计数作为一个名为_reps的关键字参数传入
3.显示最快的一次执行时间
4.可以直接在python console里面import timer或者best测试
"""

import time,sys


trace = lambda *args : None #也可以用print

timefunc = time.clock if sys.platform == 'win32' else time.time

def timer(func,*pargs,_reps=1000,**kargs):
    trace(func,pargs,kargs,_reps)
    start=timefunc()
    for i in range(_reps):
        ret = func(*pargs,**kargs)
    elapsed = timefunc() - start
    return (elapsed,ret)

def best(func, *pargs,_reps=50,**kargs):
    best=2*32
    for i in range(_reps):
        (time,ret) = timer(func,*pargs,_reps=1,**kargs)
        if time < best:best = time
    return (best,ret)