'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 11:57:23
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 11:57:23
    @Title : Increasing Order by tuple last element
'''

def create_tuple(i):
    """ 
        Description: 
            This function is creating integer list of any length
        Parameter:
            None
        Return:
            returns list
    """
    tuple_ele = ()
    no_of_elements = int(input(f"\nEnter how many numbers you want to add in tuple {i+1}: "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i+1} th value : "))
        tuple_ele = tuple_ele + (number,)

    return tuple_ele

def get_last_of_tuple(tuple):    
    """ 
        Description: 
            This function is used to get last element of tuple
        Parameter:
            tuple
        Return:
            returns last element of tuple
    """
    return tuple[-1]  
   
def sort_list_with_key(list):
    """ 
        Description: 
            This function is sorting list by key
        Parameter:
            list
        Return:
            returns sorted list
    """
    sorted_list = sorted(list, key=get_last_of_tuple)
    return sorted_list


from LoggingFile import *
logger  = func()
#Main Code
if __name__ == "__main__":
    #list =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]    
    count = int(input("\nHow many tuple you want to add in list : "))
    list=[create_tuple(i) for i in range(count)]
    sorted_list = sort_list_with_key(list)
    logger.info(f"\nSorted list based on tuple last element : {sorted_list}")
