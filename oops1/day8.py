 ########  INHERITENCE ######

class family:
    def __init__(self,surname):
        self.surname=surname        
class Child(family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name=name
child=Child("g","s")    
print(f"{child.name} {child.surname}")    

#################
class animal:
    def sound(self):
        print("animal make a sound")
class dog(animal):
    def sound(self):
        print("bark")    
class cat(animal):
    def sound(self):
        print("wow")
animals=[dog(),cat()]      
for animal in animals:
    animal.sound()  

##############

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=student("kush",2)
print(s.name)      

###########
class calculate:
    def add(self,a,b,c=0):
        print(a+b+c)
c=calculate()
c.add(1,2)    
c.add(1,2,3)    

###### METHOD OVERRIDING PARENT CLASS CHILD CLASS OVERIDE #####

class animal:
    def make_sound(self):
        print("animal is sound")

class dog(animal):
    def make_sound(self):
            print("bark")    
d= dog()
d.make_sound()   

################

class animal:
    def make_sound(self):
        print("animal is sound")

class dog(animal):
    def make_sound(self):
            print("bark")    
d= dog()
d.make_sound()   

