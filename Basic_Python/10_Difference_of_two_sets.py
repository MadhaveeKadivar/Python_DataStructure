'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 10:10:29
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 10:10:29
    @Title : Difference of two sets
'''
def list_create():
    """ 
        Description: 
            This function is used for creating list
        Parameter:
            None
        Return:
            returns list
    """
 
    no_of_elements = int(input("Enter how many numbers you want to add in list : "))
    list = [int(input(f"Enter {i+1} th value : ")) for i in range(no_of_elements)] 
    return list

from LoggingFile import *
logger = func()
if __name__ == "__main__":
    set1 = set(list_create())
    set2 = set(list_create())
    result = set1.difference(set2)
    logger.info(result)