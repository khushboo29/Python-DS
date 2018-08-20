#thread safe implemention of singleton with double checked locking pattern

import threading

class SingletonThreadSafe:
    __instance = None
    __lock = threading.Lock()
    
    def __init__(self):
        if self.__instance != None:
            raise Exception("a singleton instance already created")
            
    @classmethod
    def getInstance(cls):
        if cls.__instance ==None:
            with cls.__lock:
                if cls.__instance == None:
                    cls.__instance = SingletonThreadSafe()
        return cls.__instance
        
if __name__ == '__main__':
	class A(SingletonThreadSafe):
		pass

	class B(SingletonThreadSafe):
		pass

	a, a2 = A.getInstance(), A.getInstance()
	b, b2 = B.getInstance(), B.getInstance()

	assert a is a2
	assert b is b2
	assert a is not b

	print('a:  %s\n a2: %s' % (a, a2))
	print('b:  %s\n b2: %s' % (b, b2))
