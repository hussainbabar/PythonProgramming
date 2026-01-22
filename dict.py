d = {1:'Babar', 2:'Raju', 3:'HariPriya'}
print(d)
print(type(d))  #Output: <class 'dict'>

dic = dict({'Name':'Babar',"Age":30, "City":"Hyderabad","Company":"HCL Tech"})
print(dict)
print(type(dic))

#Accessing Values
print(dic['Name'])
print(d[2])

#updating Values
dic["Age"]=31
print(dic)
d[3] = "Surya Kranthi"
print(d)

#add elements 

dic["Country"] = "India"
print(dic)

d[4] = "Krqnthi"
print(d)

#Removing Elements
d.pop(4)
print(d)
dic.pop("Country")
print(dic)

del dic["City"]
print(dic)

del d[1]
print(d)    

del dic["Name"]
print(dic) # This will raise an error as dic is deleted

dic.popitem()
print(dic)

dic.clear()
print(dic)