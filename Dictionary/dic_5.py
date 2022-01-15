# Write a Python script to concatenate following dictionaries to create a new one.
# Shubham Dankhara 
# D21cS108

dict1={1:20,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
temp={}
for val in (dict1,dict2,dict3):
    temp.update(val)
print(temp)