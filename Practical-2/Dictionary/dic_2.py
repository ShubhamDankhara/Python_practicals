#  Write a Python script to merge two Python dictionaries.
# Shubham Dankhara 
# D21cS108

dic_1={1:10,2:20,3:30}
dic_2={4:40,5:50,6:60}
dic=dic_1.copy()
dic.update(dic_2)
print(dic)