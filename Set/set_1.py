# Write a Python program to add member(s) in a set and clear a set
# Shubham Dankhara 
# D21cS108

def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

set = {"1","2","3","4"}

items = ['a','b','c','d']
#calling function
set = addtoset(set,items)

#printing results
print(set)