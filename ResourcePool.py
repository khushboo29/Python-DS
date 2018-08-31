'''Object Pool or Resource Pool
it is most efficient way where cost of initializing a class instance is very high and rate of instantiation of a class is high, and the number of instantiations in use at one time is low
OP is used to manage the object caching i.e; manage the connection and provide a way to resuse and share them. It can also limit the maximum number of objects that can be created.
'''
class Reusable:
    pass

#manage reusable objects
class ReusablePool(object):
    def __init__(self,size):
        self._reusables = [Reusable() for _ in range(size)]
        
    def acquire(self):
        return self._reusables.pop()
        
    def release(self,reusable):
        self._reusables.append(reusable)
        
def main():
    reusable_pool = ReusablePool(10)
    print(reusable_pool);
    reusable = reusable_pool.acquire()
    print(reusable);
    reusable_pool.release(reusable)
        
if __name__ == '__main__':
    main()
