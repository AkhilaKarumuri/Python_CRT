# def function_name(parameters):
#     if base_condition:
#         return result
#     return function_name(modified_parameters)
def Add_List(n,Sum):
    if n!=0:
        Sum=Sum+n
        return Sum
    return Add_List(n-1,Sum)
print(Add_List(5,0))

def Add_List(List, Sum):
    if bool(List):
        Sum+=int(List[0])
        return Add_List(List,Sum)
    return Sum
print(Add_List([1,2,3],0))
