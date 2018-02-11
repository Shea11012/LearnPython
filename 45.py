class A:
    def __getattr__(self,name):
        return "该属性不存在"
    
class Demo:
    def __getattr__(self,name):
        self.name = 'FishC'
        return self.name
    
    
class Counter:
    def __init__(self):
        super().__setattr__('counter', 0)
    def __setattr__(self, name, value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)
    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(name)