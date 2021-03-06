'''Ensure a class has only one __instance, and provide a global point of access to it.
single set of data state in all objects '''

#this is implemented with lazy initalization

''' Lazy instantiation makes sure that the object gets created when it's actually needed
In the following code example, when we say s=Singleton(), it calls the __init__ method but no new object gets created. However, actual object creation happens when we call Singleton.Instance(). This is how lazy instantiation is achieved.'''

class Singleton(object):
    __instance = None;
    
    def __init__(self):
        if self.__instance != None:
            raise ValueError("A Singleton instance is already exisiting")
    
    @classmethod
    def Instance(cls):
        if cls.__instance == None:
            cls.__instance = Singleton()
        return cls.__instance
        
    def setData(self,num):
        self.data = num
        
    def getData(self):
        return self.data
        
o1 = Singleton.Instance();
o2 = Singleton.Instance();
#o3 = Singleton.Instance().setData(30);
d1 = Singleton.Instance();
print(d1)
print(o1)
print(o2)
