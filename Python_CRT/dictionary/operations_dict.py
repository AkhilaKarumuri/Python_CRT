jobrole={1:'Full stack developer',2:'Front end engineer',3:'Back end engineer',4:'cloud engineer'}
print(jobrole)
jobrole[5]='Datascientist'
jobrole[6]='Dataanalyst'
jobrole[7]='Dataengineer'
print(jobrole)
jobrole.pop(7)
print(jobrole)
del jobrole[4]
print(jobrole)
print(len(jobrole))
print(jobrole.keys())
print(jobrole.values())
# items():- returns a list of key-value pairs as tuples in the dictionary
print(jobrole.items())
# update--> adds two different dictionaries
dict1={1:'a',2:'b',3:'c'}
print(dict1)
dict2={4:'d',5:'e',6:'f'}
dict1.update(dict2)
print(dict1)
