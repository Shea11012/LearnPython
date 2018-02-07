# 算术运算
#从A-B 将A中所有B的子字符串减去
class Nstr(str):
    def __sub__(self,other):
        return self.replace(other,'')
a = Nstr('I love Fishc!iiiiii')
b = Nstr('i')
print(a - b)

#将位移操作符计算重写
class Nstr(str):
    def __lshift__(self,other):
        return self[other:] + self[:other]
a = Nstr('I love Fishc!')
print(a << 3)


#将字符串变成ASCII码计算
''' class Nstr:
    
    def __init__(self,arg):
        if isinstance(arg,str):
            self.total = 0
            for i in arg:
                self.total += ord(i)
        else:
            print('参数错误')
    
    def __sub__(self,other):
        return self.total - other.total '''
#将字符串变成ASCII码计算方法2
class Nstr(int):
    def __new__(cls,arg=0):
        if isinstance(arg,str):
            total = 0
            for i in arg:
                total += ord(i)
            arg = total
        else:
            print('参数错误')
        return int.__new__(cls,arg)
a = Nstr('ni hao')
b = Nstr('hello')
print(a - b)