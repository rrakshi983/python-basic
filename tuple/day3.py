#########tuple is used to store the values in one varia

######APPEND METHOD######

fruits=("apple","banana","orange")
print(fruits[0])


###########NEGETIVE INDEXING######
fruits=("apple","banana","orange")
print(fruits[-1])

###tuple slicing###
num=(10,20,30,40,50)
print(num[1:4])

num=(10,20,30,40,50)
print(num[:4])

num=(10,20,30,40,50)
print(num[:])

num=(10,20,30,40,50)
print(num[::-1])


#########count######
num=(10,20,30,40,10,50)
print(num.count(10))


######len######
num=(10,20,30,40,10,50)
print(len(num))

#####find the position of element######
num=(10,80,30,40)
print(num.index(10))

####create empty list#######
tuple=()
print(tuple)

######convert tuple to list#num=[10,80,30,40]

# num=[10,80,30,40]
# my_tuple=tuple(num)
# print(my_tuple)


a=(10,)
print(a)
