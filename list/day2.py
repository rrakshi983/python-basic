###############list is the used to store te multiple values in single variable#######

num=[1,2,3,4]
print(num)

######APPEND METHOD######

num=[]
num.append(10)
num.append(20)
print(num)

fruits=["apple","banana","orange"]
print(fruits[0])


###########NEGETIVE INDEXING######
fruits=["apple","banana","orange"]
print(fruits[-1])

###########ADD ELEMENT####

fruits=["apple","banana","orange"]
fruits.append("mango")
print(fruits)


#######ADD ELEMENT IN SPECIFIC POSITION########

fruits=["apple","banana","orange"]
fruits.insert(2,"mango")
print(fruits)

########ADD MULIPLE VALUES######
 
fruits=["apple","banana","orange"]
fruits.extend(["mango","grapes"])
print(fruits)


##########REMOVE########

fruits=["apple","banana","orange"]
fruits.remove("apple")
print(fruits)

######remove useing index######


fruits=["apple","banana","orange"]
fruits.pop(1)
print(fruits)

########useing del######

fruits=["apple","banana","orange"]
del fruits[1]
print(fruits)


#########list slicing#######

num=[10,20,30,40,50]
print(num[1:4])

num=[10,20,30,40,50]
print(num[:4])

num=[10,20,30,40,50]
print(num[:])


########REVERSE SLICING#########

num=[10,20,30,40,50]
print(num[::-1])

####LOOP THROUGHT LIST####

numbers=[10,20,30,40,50]
for num in numbers:
    print(num)

####### list in range####

num=list(range(1,6))
print(num)

#####sort in a list####

num=[10,80,30,40]
num.sort()
print(num)

####sort in desendig order#####

num=[10,80,30,40]
num.sort(reverse=True)
print(num)

num=[10,80,30,40]
num.reverse()
print(num)

#######count#####

num=[10,80,10,30,40]
print(num.count(10))

####index########

num=[10,80,30,40]
print(num.index(10))

########min and max####
num=[10,80,30,40]
print(min(num))

num=[10,80,30,40]
print(max(num))


#######sum########
num=[10,80,30,40]
print(sum(num))

