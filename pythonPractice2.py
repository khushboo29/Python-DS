class Person(object):
    def __init__(self,name):
        self.name = name
    
    def reveal_identity(self):
        print('my name is {}'.format(self.name))
    
class SuperHero(Person):
    def __init__(self,name,hero_name):
        super().__init__(name) #right
        #Person.__init__(self,name) #right
        #super(SuperHero,self).__init__(name) #right but notclear
        self.hero_name = hero_name
        
    def reveal_identity(self):
        super().reveal_identity() #right
        #Person.reveal_identity(self) #right
        #super(SuperHero,self).reveal_identity() #right but notclear
        print('...and i\'m super hero {}'.format(self.hero_name))
    
per1 = Person('Khush')
per2 = SuperHero('Ajay','batman')
per1.reveal_identity()
per2.reveal_identity()
