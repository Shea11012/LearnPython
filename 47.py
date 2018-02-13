class Test:
    def __init__(self,*arg):
        self.arg = [x for x in range(1,len(arg)+1,1)]
        self.count = {}.fromkeys(range(1,len(self.arg)+1,1),0)
    
    def __len__(self):
        return len(self.arg)

    def __getitem__(self,key):
        # count = 0
        if self.arg[key-1] in self.count:
            self.count[self.arg[key-1]] += 1
        else:
            self.count[self.arg[key-1]] = 1
        return self.arg[key-1],self.count[self.arg[key-1]]

    def __setitem__(self,key,value):
        if key in self.arg:
            if value in self.count:
                self.count[self.arg[key]] += 1
        else:
            self.arg.insert(key,value)
            self.count[value] = 1
    
    def __delitem__(self,key):
        if key in self.arg:
            if self.count.get(key) != 'None':
                del self.count[self.arg[key-1]]
                del self.arg[key-1]
        
    def __reversed__(self):
        self.arg = self.arg[::-1]

    def append(self,value):
        if value in self.arg:
            if self.count.get(value) != 'None':
                self.count[value] += 1
        else:
            self.arg += [value]
            self.count[value] = 1
    
    def pop(self,index=-1):
        if index > len(self.arg):
            print('输入的下标超过列表的大小')
        else:
            if self.arg[index] in self.arg:
                if self.arg[index] in self.count:
                    del self.count[self.arg[index]]
                    value = self.arg[index]
                    del self.arg[index]
            return value

    def remove(self,value):
        if value in self.count:
            del self.count[value]
            if value in self.arg:
                for i in range(len(self.arg)-1):
                    if value == self.arg[i]:
                        del self.arg[i]

    def insert(self,index,value):
        if value in self.arg and value in self.count:
            self.count[value] += 1
        else:
            before = self.arg[:index]
            after = self.arg[index:]
            before += [value]
            self.arg = before + after
            self.count[value] = 0

    def clear(self):
        self.arg = []
        self.count = {}
                
## 小甲鱼写的，小甲鱼说字典记录访问次数不合适但是我没看出问题
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
