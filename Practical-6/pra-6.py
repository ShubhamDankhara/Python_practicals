# Some words may repeat
# D21CS108
# Shubham Dankhara

def unique(lst):
    uniq = list()
    return [x for x in lst if not (x in uniq or uniq.append(x))]

# Taking length input
s= int(input())

# taking words input in list
lst = []
for i in range(s):
    lst.append(input())

# Creating a list having unique items
new_list = unique(lst)

# Creating a list having count of items
output = []
for i in new_list:
    output.append(lst.count(i))

# Printing length and items of list
print(len(output))
print(*output)