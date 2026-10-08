###### dictonary is used store the data in key value pairs#####

student={"name":"rakshitha","age":20,"course":"engineering"}
print(student)

student={"name":"rakshitha","age":20,"course":"engineering"}
print(student["name"])

student={"name":"rakshitha","age":20,"course":"engineering"}
print(student["age"])


###  get method()    ########
student={"name":"rakshitha","age":20,"course":"engineering"}
print(student.get("name"))

##### Add new item  dictonary  ####

student={"name":"rakshitha","age":20,"course":"engineering"}
student["city"]="Hassan"
print(student)

#### Delete items ###

student={"name":"rakshitha","age":20,"course":"engineering"}
del student["name"]
print(student)

#### pop item() method  #######

student={"name":"rakshitha","age":20,"course":"engineering"}
student.popitem()
print(student)


#### clear() method #######

student={"name":"rakshitha","age":20,"course":"engineering"}
student.clear()


########key() ########

student={"name":"rakshitha","age":20,"course":"engineering"}
print(student.keys())
 
######## values()######

student={"name":"rakshitha","age":20,"course":"engineering"}
print(student.values())

##########item()########

student={"name":"rakshitha","age":20,"course":"engineering"}
print(student.items())

######## for loop #######

student={"name":"rakshitha","age":20,"course":"engineering"}
for key in student:
    print(key)

#############values####
student={"name":"rakshitha","age":20,"course":"engineering"}
for value in student.values():
    print(value)

#######items######

student={"name":"rakshitha","age":20,"course":"engineering"}
for key,value in student.items():
    print(key,value)

######check whether key is exist####
student={"name":"rakshitha","age":20,"course":"engineering"}
if "name" in student:
    print("name exiests")

#######len #######

student={"name":"rakshitha","age":20,"course":"engineering"}
print(len(student))

#####duplicate the keys######
student={"name":"rakshitha","name":"ruchi"}
print(student)

###### list instade of dictonary######
student={"name":"rakshitha","subject":["ai","ml","python"]}
print(student["subject"])


#########index give abd value find#####3
student={"name":"rakshitha","subject":["ai","ml","python"]}
print(student["subject"][0])

######dictonary instade of dictonary#####
students={"student1":{"name":"rakshitha","age":20},
"student2":{"name":"raksha","age":21}}

#####update  method#####3
student={"name":"rakshitha","age":20}
student.update({"city":"hassan"})
print(student)

#####copy method#######

student={"name":"rakshitha","age":20}
new_student=student.copy()
print(new_student)


####create empty dictonaries######

student={}
print(student)

  ##### or  #####
 
student=dict()
print(student)

###  dictonary comprehension ########

numbers={x:x*2 for x in range(1,6)}
print(numbers)


######sort######

marks={"anu":56,"kush":69,"ramu":54}
print(sorted(marks))



marks={"anu":56,"kush":69,"ramu":54}
print(sorted(marks.values()))

####find hightest value  ######


marks={"anu":56,"kush":69,"ramu":54}
high=max(marks.values())
print(high)

####dict construct#####3

students=dict("name:"banu,"age:56")
print(students)


####### convert list into dictonary  ####

keys=["anu","raja"],
values=[45,69]
student=dict(zip(keys,values))
print(student)

######range #####
numbers=list(range(5))
print(numbers)






