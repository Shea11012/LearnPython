# 定义的模块，模块必须在python的根目录下
# class Const:
    
#     def __setattr__(self,name,value):
#         if name in self.__dict__:
#             raise TypeError('常量无法改变')
        
#         if not name.isupper():
#             raise TypeError('常量名必须由大写字母组成')

#         self.__dict__[name] = value
    
# sys.modules是一个字典，它包含了python从开始运行起，被导入的所有模块。键就是模块名，值就是模块对象
# import sys
# sys.modules[__name__] = Const()


import const

const.NAME = 'FishC'
print(const.NAME)

try:
    const.NAME = 'FishC'
except TypeError as Err:
    print(Err)

try:
    const.name = 'FishC'
except TypeError as Err:
    print(Err)