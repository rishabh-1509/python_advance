#This file contains all the advance dictionary function 
mydict = {"name":"Rishabh","age":"21","city":"New York"}

# Another way to define dictionary using dict function 
newdict = dict( name = 'Rishabh', age = 21, city= "new york ")

# calling the keys form the dictionary 
value  = mydict["name"]
#add the value to the dictionary
mydict["email"] = "rishabh@xyz.com"
#delete the item in the dictionary using del function 
del mydict["age"]
mydict.pop("emai")
mydict.popitem()# Removes the last item form the dictionary 

# if statement in dictionary
if "name " in mydict:
    print("present ")
else:
    print("not present")

# try and exect method 

    try:
        print(mydict["city"])
    except KeyError:
        print("key not found")
# some inbuilt method 
mydict.keys()# Return all the Keys in the Dictionary
mydict.values()# Return all the Values in the Dictionary
# Looping in dictionary 

# using for in loop
for key in mydict:
    print(key)
# accessing both keys and values
for key,value in mydict.items():
    print(key,value)
# copying the dictioary 
# first method using assingment opretor 
mydict_copy = mydict# changes made in mydict_copy will affect the  original

# using built in copy function
mydict_copy.copy(mydict)

#using update function in python 
mydict_copy.update(mydict)
# using integer as a key 
new_dict = {1:2,3:4,5:6}
# using tuple as a key 
mytuple  = (3,4)
tup_dict = {mytuple:7}
