class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def display_info(self):
        print(f"brand:{self.brand},model:{self.model}")
my_car=car("toyota","bmw")
my_car.display_info()        



###############
class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print(f"{self.name},{self.age} years young lady  is running")
rakshitha=human("rakshitha",20)
rakshitha.run()

########

class student:
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks
    def enquiry(self):
        print(f"{self.name} has scored {self.marks} marks")
student1=student("raksha",90)
student1.enquiry()     

##########
class human:
    def __init__(self,name,age,salary=-1):
        self.name=name
        self.age=age
        self.salary=salary
    def run(self):
        print(f"{self.name},{self.age} years young lady  is running")
R=human("rakshitha",20,50000)
s=human("sun",20)
print(R.salary)

############
class human:
    def __init__(self,name="unknown",age=0,salary=-1):
        self.name=name
        self.age=age
        self.salary=salary
    def run(self):
        print(f"{self.name},{self.age} years young lady  is running")
R=human("rakshitha",20,50000)
s=human("sun",20)
print(R.salary)

paapu=human()
paapu.name="paapu"
paapu.run()

