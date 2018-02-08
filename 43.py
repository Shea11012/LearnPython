# 算数运算2
class C:
    def __init__(self,*arg):
        if not arg:
           print('并没有参数传入')
        else:
            print('传入%d个参数，分别是：'% len(arg),end='')
            for i in arg:
                print(i,end=' ')
#自己写的
class Word(str):
    def __init__(self,arg):
        self.words = arg.split(' ')
    #小于
    def __lt__(self,other):
        return len(self.words[0]) < len(other.words[0])

#小甲鱼写的         
class Word(str):
'''存储单词的类，定义比较单词的几种方法'''

    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

