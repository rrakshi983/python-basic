#######FUNCTIONS######
def greet():
    print("welcome")
greet()    

########FUNCTIONS print 3 times######
def greet():
    print("welocome to the functions")
greet()
greet()
greet()    


#####FUNCTION WITH RETURN VALUE####
def greet():
    return "welcome to raksha's world"
print(greet())


##### FUNCTION USEING FARMATED STRING###
def greet(name):
    print(f"hello,{name}%")
greet("raksha") 

#######FUNCTION IN SUM #####

def greet(a,b):
    return a+b
result=greet(5,6)
print(result)    

######FUNCTION IN MULTIPLICATION #######
def my_name(r,s):
    return r*s
answer=my_name(5,8)
print(answer)


############

def greet(age,name):
    print(age)
    print(name)
greet(12,"raksha")

############### USEING FORMATED STRING ####

def greet(size="small"):
    print(f" my size is  {size}")
greet("large")
greet()

#######

def greet(name):
    print("hello",name)
greet("rakshitha")  

#######

def squre(number):
    print(number*number)
x=squre(5)
print(x)

#####

def student(name,age):
    print(name)
    print(age)
student(name="raksha",age=12)


#######

def greet(name,age):
    print(name)
    print(age)
greet("raksha",20)   


###########

def add(*numbers):
    print(numbers)
add(1,2,3,5,6)    


########### FUNCTIONS USEING FOR LOOP#####

def add(*numbers):
    total=0
    for number in numbers:
        total=total+number
    return total
print(add(1,2,3,4,5,6))


###########

name="raksha"
def greet():
    print(name)
greet()

########

squre=lambda number:number*number
print(squre(5))


######### FUNCTIONS USEING LAMBDA FUNCTION####

a=lambda a,b:a+b
print(a(1,2))

#####
b=lambda a:2*a
print(b(100))


######### FUNCTIONS USEING SORT IN REVERSE #######
students=[
    {"name":"raksha","age":12},
    {"name":"gowda","age":15}]
students.sort(key=lambda x:x["age"],reverse=True)
print(students)


 ############ FUNCTIONS USEING SORT #######
students=[
    {"name":"raksha","age":12},
    {"name":"gowda","age":15}]
students.sort(key=lambda x:x["age"],reverse=True)
print(students)

####RECRSION FUNCTION CALLING IT SELF ######

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))  

########################
def sum(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    def mult():
        return a*b
    print(add())   
sum(1,7)   

###########
def add(name,*,age,course):
    print(name,age,course)
add("rakshita",age=12,course="B E")

##########
def add(name,/,*,age,course):
    print(name,age,course)
add("rakshita",age=12,course="B E")

##########
def add(a:int,b:int)->int:
    return a+b
print(add(12,6))    


######

def outer(x):
    def inner():
        return x
    return inner
result=outer(10)
print(result())

#######
       



    


 
