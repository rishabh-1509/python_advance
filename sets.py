# Sets : unordered , mutable , no duplicates 
myset = {1,2,3,4}
#instilzong the empty set 
empset = set()
#adding elements in empty set using add method
empset.add(1)
empset.add(2)
empset.add(3)
empset.add(4)
empset.add(5)
#remove method for the set 
empset.remove(1)
empset.discard(3)
empset.clear()#this will empty the list 
empset.pop()#return the last element from the set
# itreation of sets 
for i in empset:
    print(i)
# checking for the element in the set 
if 1 in empset:
    print(" good set")
else:
    print("bad set")

# Union of two sets
odds = {1,3,5,7,9,}
evens = {0,2,4,6,8,}
prime = {2,3,5,7}
u = odds.union(evens) # will combine the sets form   
# intersection of the elements
itnernsec = odds.intersection(prime) # retun the common elements in the two functions

# difference between two set
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)# gives the elements that are not present in the firstset 
#symmetric difference
diff = setB.symmetric_difference(setA)# give all the common element but not the uncommon elements 
# update method 
setA.update(setB)
# intersection update
setA.intersection_update(setB)# update the sets with elements found in both the sets 
#diffrenece update 
setA.difference_update( setB)# update the sets with elements not found in both sets
