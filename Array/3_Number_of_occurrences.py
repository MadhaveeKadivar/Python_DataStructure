'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 07:36:29
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 07:36:29
    @Title : Find number of occurrence 
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
def occurrence(num_arr,num):
    """ 
        Description: 
            This function is counting number of occurrence of any specific number in arary
        Parameter:
            It takes array and any specific number as argument
        Return:
            number of occurrence
    """
    count = 0
    for i in num_arr:
        if i == num :
            count +=1
    return count
    
#Main Code
if __name__=="__main__":
    total_numbers = int(input("\nEnter how many numbers you want to add in array : "))
    num_arr = create_array(total_numbers)
    print_array(num_arr)
    num = int(input("Enter any number : "))
    num_of_occurrence = occurrence(num_arr,num)
    logger.info(f"Numbers of occurrence of {num} are : {num_of_occurrence}")