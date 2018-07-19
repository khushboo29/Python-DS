#Duck typing and easy forgiveness,not permission

class Duck:
    def quack(self):
        print("Quack Quack")
    def fly(self):
        print("Flap Flap")
        
class Person:
    def quack(self):
        print("Quacking like Duck")
    def fly(self):
        print("Flying like a Duck")

def quack_fly(object):
    #non pythonic way1
#    if(isinstance(object,Duck)):
#        object.quack()
#        object.fly()
#    else:
#        print("instance should have Duck type")

    #non pythonic way2
    if(hasattr(object,'quack')):
        if callable(object.quack):
            object.quack()
    if hasattr(object,'bark'):
        if callable(object.bark):
            object.bark()

    #pythonic way
#    try:
#        object.quack()
#        object.fly()
#        object.bark()
#    except AttributeError as e:
#        print(e)
#    print()

d=Duck()
quack_fly(d)
p=Person()
quack_fly(p)
