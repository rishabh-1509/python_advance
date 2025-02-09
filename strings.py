#string ordered,immutable ,text rpresentation
my_string = "hello world"

# accessing string elements using index
chat = my_string[0]
print(chat)
#slicing the string 
substring = my_string[1:5]
print(substring)
#looping through string elements
for i in my_string:
    print(i)
#strip Removing the whitespace

my_string = my_string.strip()
print(my_string)
#uppercase and lowercase 
my_string = my_string.lower()
my_string = my_string.upper()
# find method 
print(my_string.find('h'))#return the index of the h in the string 
#count method 
print(my_string.count('o'))#return the number of o in the string 
#replace method 
my_string = my_string.replace('world','universe ')
print(my_string)
#converting the string into list 
my_string = my_string.split()#default value of using space as a delimter and we can use , also
print(my_string)
#converting the list back into string 
new_string = ''.join()

