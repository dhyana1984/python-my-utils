'''
单例模式装饰器
'''

#用函数装饰器实现
def singletonFunc(aClass): 
    instance = None
    def onCall(*args): 
        nonlocal instance 
        if instance == None:
            instance = aClass(*args) 
        return instance
    return onCall

#用类实现
class singletonCls:
    def __init__(self, aClass): 
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args): 
        if self.instance == None:
            self.instance = self.aClass(*args) 
        return self.instance