#without using the in-built functions
# list=[12,24,67,98,98,76,24]
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)
# print(new)

# #by set method
# list_ = [12, 24, 67, 98, 98, 76, 24]
# unique_list = list(set(list_))
# print(unique_list)

#
list=["car","barbie","car","bike"]
new=[]
for i in list:
    if i not in new:
        new.append(i)
print(new)

''' wap to read marks of 5 students for 3 subjects each and print the marks list for individual student along with the class where 
students marks >90 -- 1st class
students marks >75 -- 2nd class
students marks >50 -- 3rd class
students marks <50 -- Fail'''