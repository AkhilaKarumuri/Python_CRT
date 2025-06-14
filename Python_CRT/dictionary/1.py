# Syntax:- dict_name={key1:value1,key2:value2}
dict={1:'Python',2:'Java',3:'C',4:'C++'}
print(dict)
print(type(dict))
print(dict[2])

"""Key should be unique
If we mention same key again, the old key will be overwritten
key should be immutable type ex:-Integer, string or tuple 
We can not use list or dictionary as key
String can be given as key as it is immutable"""

stu={1:'Amulya',2:'Akhila',3:'Rahul'}
fees={'Amulya':20000,'Akhila':15000,'Rahul':30000}
print(stu[1])
print(stu[2])
print(stu[3])
print(fees['Amulya'])
print(fees['Akhila'])
print(fees['Rahul'])
fees['Rahul']=25000
print(fees['Rahul'])