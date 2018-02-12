import time
import os
import pickle
#摄氏度
class Celsius:
    def __init__(self,value=25.0):
        self.value = float(value)

    def __get__(self,instance,owner):
        return self.value

    def __set__(self,instance,value):
        self.value = float(value)
        
#华氏度
class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.celsius * 1.8 + 32

    def __set__(self,instance,value):
        instance.celsius = (float(value)-32)/1.8

class Temperature:
    
    celsius = Celsius()
    fahrenheit = Fahrenheit()

# class Mydes:
#     def __init__(self,value,arg):
#         self.value = value
#         self.arg = arg
    
#     def __get__(self,instance,owner):
#         print("正在获取变量:{}".format(self.arg))
#         return self.value
    
#     def __set__(self,instance,arg):
#         print('正在修改变量：%s' % self.arg)
#         self.arg = arg
    
#     def __delete__(self,instance):
#         print('正在删除变量：%s' % self.arg)
#         if self.arg == 'x':
#             print('噢~这个变量删除不了~')
#         else:
#             del self.arg


class Record:
    def __init__(self,num,value):
        self.num = num
        self.value = value
        self.name = 'record.txt'
        self.time = time.strftime("%a %b %d %H:%M:%S %Y")

    
    def recordfile(self,content):
        try:
            with open(self.name,'x+',encoding='utf-8') as f:
                f.write(content)
        except FileExistsError:
            with open(self.name,'r+',encoding='utf-8') as f:
                f.write(content)

    def __get__(self,instance,owner):
        content = "{} 变量于北京时间 {}被读取，{} = {}\n".format(self.value,self.time,self.value,self.num)
        self.recordfile(content)
        return self.value
    def __set__(self,instance,value):
        self.value = value
        content = "{} 变量于北京时间 {}被修改，{} = {}\n".format(self.value,self.time,self.value,self.num)
        
    # def __delete__(self,instance):

class Mydes:
    def __init__(self,value,num=None):
        self.num = num
        self.value = value
        self.time = time.strftime("%a %b %d %H:%M:%S %Y")

    def pklfile(self,filname):
        try:
            with open(filname,'xb+') as f:
                pickle.dump(self.num,f)
        except FileExistsError:
            with open(filname,'wb+') as f:
                pickle.dump(self.num,f)

    def __get__(self,instance,owner):
        # content = "{} 变量于北京时间 {}被读取，{} = {}\n".format(self.value,self.time,self.value,self.num)
        # self.pklfile(content)
        return self.num
    
    def __set__(self,instance,num):
        self.num = num
        filename = self.value + '.pkl'
        # content = "{} 变量于北京时间 {}被修改，{} = {}\n".format(self.value,self.time,self.value,self.num)
        self.pklfile(filename)
    
    def __delete__(self,instance):
        rootfile = os.listdir()
        for i in range(len(rootfile)):
            if os.path.isfile(rootfile[i]):
                if rootfile[i] == self.value + '.pkl':
                    os.remove(self.value+'.pkl')
        del self.value

class Test:

    x = Mydes('x')
    y = Mydes('y')

