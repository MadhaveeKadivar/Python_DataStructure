'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 19:12:25
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 19:12:25
    @Title : Remove element from tuple
'''
def remove_ele(tuple_ele,element):
    """ 
        Description: 
            This function is removing element from tuple
        Parameter:
            It takes one tuple and one element as argument
        Return:
            returns tuple 
    """
    new_list = list(tuple_ele)
    c = new_list.count(element)
    for i in range(c):
            new_list.remove(element)
    return tuple(new_list)

if __name__=="__main__":
    tuple_ele = ()
    no_of_elements = int(input("\nEnter how many numbers you want to add in tuple : "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i+1} th value : "))
        tuple_ele = tuple_ele + (number,)
    element = int(input("\nEnter which element you want to remove from tuple : "))
    new_tuple = remove_ele(tuple_ele,element) # calling function
    print(f"\nModified tuple : {new_tuple}\n")