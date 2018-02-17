import datetime
class LeapYears:

    def __init__(self,):
        self.now_year = datetime.date.today().year
    
    def isleapyear(self,year):
        if (year%4==0 and year%100!=0) or year%400==0:
            return True
        else:
            return False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while not self.isleapyear(self.now_year):
            self.now_year -= 1
        temp = self.now_year 
        self.now_year -= 1
        return temp
       
# leapyear = LeapYears()
# for year in leapyear:
#     if year>2000:
#         print(year)
#     else:
#         break


class MyRev:
    def __init__(self,arg):
        self.arg = arg
        self.index = len(self.arg)

    def __iter__(self):
        return self
    
    def __next__(self):
        #这个是小甲鱼的方法
        #--------------------
        # if self.index == 0:
        #     raise StopIteration
        # self.index -= 1
        # return self.arg[self.index]
        # ---------------------------
        while(self.index):
            self.index -= 1
            return self.arg[self.index]
myrev = MyRev('FishC')
for i in myrev:
    if i != None:#不按小甲鱼的方法会不停的返回None，所以需要一个判断停止None输出
        print(i,end='')
    else:
        break