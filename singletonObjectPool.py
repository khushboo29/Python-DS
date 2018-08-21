'''Object Pool'''
'''limit on total number created instances'''
class limitedSingleton(object):
    __instance = [];
    limit = 5
    
    @classmethod
    def Instance(cls):
        if not len(cls.__instance) < cls.limit:
            raise Exception("keep in your limits")
        instance = limitedSingleton()
        cls.__instance.append(instance)
        return instance

o1 = limitedSingleton.Instance();
o2 = limitedSingleton.Instance();
d1 = limitedSingleton.Instance();
d2 = limitedSingleton.Instance();
print(o1)
print(o2)
print(d1)
print(d2)
