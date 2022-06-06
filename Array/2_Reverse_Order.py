'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 07:19:34
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 07:19:34
    @Title : Reverse order Array
'''
# Importing module of array
import array as arr
from LoggingFile import func
logger = func() 
def create_array(length):
    """ 
        Description: 
            This function is creating integer array of any length
        Parameter:
            It takes length of array as argument
        Return:
            returns array
    """
    num_array = arr.array('i', [])
    for i in range(length):
        number = int(input(f"Enter {i} th number : "))
        num_array.append(number)
    return num_array
def print_array(num_arr):
    """ 
        Description: 
            This function is printing array element
        Parameter:
            It takes array as argument
        Return:
            Nothing
    """
    logger.info("[ ",end = '')
    for i in num_arr:
        logger.info(i ,end = " ")
    logger.info("]")
def reverse_order(num_arr):
    """ 
        Description: 
            This function is reversing array element
        Parameter:
            It takes array as argument
        Return:
            reverse array
    """
    num_arr = num_arr[::-1]
    return num_arr
    
# MAin Code
if __name__=="__main__":
    total_numbers = int(input("\nEnter how many numbers you want to add in array : "))
    num_arr = create_array(total_numbers)
    print_array(num_arr)
    num_arr = reverse_order(num_arr)
    print_array(f"Array in reverse order : {num_arr}")
