'''Singleton base class
in more pythonic way'''

import threading
from functools import wraps

def singleton_new(make_instance):
    lock = threading.Lock()
    instance = None

    @wraps(make_instance)
    def __new__(cls):
        nonlocal instance

        if instance is None:
            with lock:
                if instance is None:
                    instance = make_instance(cls)

        return instance

    return __new__
    
class Logger:
    @classmethod
    @singleton_new
    def get_instance(cls):
        return super().__new__(cls)
    #@singleton_new
    #def __new__(cls):
    #    return super().__new__(cls)

    def log(self, text):
        print(text)
