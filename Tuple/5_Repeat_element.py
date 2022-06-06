'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 18:29:33
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 18:29:33
    @Title : Find repeat items
'''

def find_repeat_ele(tuple_ele):
    """ 
        Description: 
            This function is finding repeating element from tuple
        Parameter:
            It takes one tuple as argument
        Return:
            returns tuple of repeated items
    """
    new_tuple = []
    for i in tuple_ele:
        if tuple_ele.count(i) > 1:
            new_tuple.append(i)
    return tuple(set(new_tuple))

if __name__=="__main__":
    tuple_ele = ()
    no_of_elements = int(input("\nEnter how many numbers you want to add in tuple : "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i+1} th value : "))
        tuple_ele = tuple_ele + (number,)
    repeat_items = find_repeat_ele(tuple_ele) # calling function
    print(f"\nRepeated item in tuples are : {repeat_items}\n")
                    
    