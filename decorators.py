class Deco():
    def my_deco(func):
        def wrapper(*args,**kwargs):
            print('in deco')
            return func(*args,**kwargs)
            print('out deco')
        return wrapper

    @my_deco
    def mSum(self,a,b):
        return a + b
    @my_deco
    def test(self):
        return 'Hello'


class1 = Deco()
print(class1.test())
print(class1.mSum(1,5))