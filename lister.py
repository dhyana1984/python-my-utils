'''
列出类树中每个对象的属性
使用一个生成器表达式来导向对超类的递归调用
'''
class ListInstance:
    def __str__(self): #如果显示实例属性使用getattr()函数的话，这里不能用repr，因为函数会除法repr，repr又会调用函数，形成死循环
        self.__visited={}
        return f'<Instance of {self.__class__.__name__}, adress {id(self)}: \n{self.__attrnames(self,0)}{self.__listclass(self.__class__,4)}>'
    def __listclass(self,aClass,indent):
        dots = '.'*indent
        if aClass in self.__visited:
            return f'\n{dots}<Class {aClass.__name__}:, address {id(aClass)}: (see above)>\n'
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c,indent+4) for c in aClass.__bases__)
            r = ''.join(genabove)
            return f'\n{dots}<Class {aClass.__name__}, address {id(aClass)}:\n{self.__attrnames(aClass,indent)}{r} {dots}>\n'

    def __attrnames(self,obj,indent):
        spaces = ' '*(indent +4)
        result=''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + f'{attr}=<>\n'
            else:
                result += spaces + f'{attr}={getattr(obj,attr)}\n'
        return result
