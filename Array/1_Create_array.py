'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 07:02:45
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 07:02:45
    @Title : Create Array
'''
# Importing module of array
import array as arr
logger = func()  
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


#Main Code
if __name__=="__main__":
    total_numbers = int(input("\nEnter how many numbers you want to add in array : "))
    num_arr = create_array(total_numbers)
    print_array(num_arr)
    logger.info(num_arr[1])
    num_arr[1] = 5 # Accessing array element using index
    print_array(num_arr)
