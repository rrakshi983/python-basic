######## DATA DRIVEN #####

def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def dev(a,b):
    return a/b
def sub(a,b):
    return a-b
def choice():
    print("simple calculater")
    print("1.add\n2. mult\n3. dev\n4.sub\n5. exit")
while True:
    choice()
    ch=int(input("enter your choice:"))
       
    if choice in {1,2,3,4}:
       a=int(input("enter the first number:"))
       b=int(input("enter the second number:"))
       if ch==1:
        print("result:",add(a,b))

       elif ch==2:
        print("result:",mult(a,b))

       elif ch==3:
        print("result:",dev(a,b))
                
       elif ch==4:
        print("result:",sub(a,b))
       elif ch==5:
        print("exit ")
        break
                
       else:
        print("choice end")             