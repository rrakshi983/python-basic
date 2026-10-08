##  set is a collection of value used to store the unique elements ###

numbers={1,2,3,4}
print(numbers)


##### Create empty sets  #####

numbers=set()
print(numbers)

###  OR  ###

numbers={}
print(numbers)

## SET DOES NOT SUPPORTING INDEXING  ##

numbers={1,2,3,4}
numbers.add(5)
print(numbers)

#####  adding a duplicate element  ##

numbers={1,2,3,4}
numbers.add(1)
print(numbers)

######## add multiple values in a set ####

numbers={1,2,3,4}
numbers.update([5,6,7])
print(numbers)


###  remove the set element ####
numbers={1,2,3,4}
numbers.remove(4)
print(numbers)

#### discard method ######
numbers={1,2,3,4}
numbers.discard(4)
print(numbers)

### pop () method  ###
##### random element is removed in set###
numbers={1,2,3,4}
numbers.pop()
print(numbers)


# clear####

numbers={1,2,3,4}
numbers.clear()
print(numbers)


#### len ###3
numbers={1,2,3,4}
print(len(numbers))

##### check the elements #

fruits={"apple","bannana","orange"}
print("apple" in fruits)

#union##
#### IT PRINT BOTH A AND B ELEMENTS#
a={1,2,3,4}
b={5,6,7,8}
print(a|b)

####### or #####
a={1,2,3,4}
b={5,6,7,8}
result=a.union(b)
print(result)

# intersection###
### IT PRINT COMMON ELEMENTS IN TO VARIABLE #####
a={1,2,3,4}
b={5,3,8}
print(a&b)

######or######

a={1,2,3,4}
b={5,6,7,8}
result=a.intersection(b)
print(result)

### defferentiation####
a={1,2,3,4}
b={5,6,7,8}
print(a-b)

####### symmetric defferentiation #####
##### it is a set but not in both ####
a={1,2,3,4}
b={5,6,7,8}
print(a^b)

##### issubset set#####
a={1,2,3,4}
b={5,8}
print(a.issubset(b))


#######a s elements is completelly inside of b  #########
a={1,2}
b={1,2,3,4,5}
print(a.issubset(b))

######set comparision ##
a={1,2,3}
b={1,2,3}
print(a==b)


### set from Tuple ##
numbers=(1,2,3,5)
result=set(numbers)
print(result)

