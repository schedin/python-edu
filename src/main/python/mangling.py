'''

'''

class Parent(object):


    def __init__(self):
        self.__update()
    
    def update(self):
        print("update in MyClass")
    
    __update = update
    
    
class Child(Parent):
    
    def update(self):
        print("update in Child")
        


c = Child()
c.update()

print(dir(c))

print(type(c._Parent__update))
