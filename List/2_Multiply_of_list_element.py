'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 10:52:32
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 10:52:32
    @Title : Multiply of list element
'''
def mul(list):
    """ 
        Description: 
            This function is used to calculate multiplication of all list element
        Parameter:
            It takes list as argument
        Return:
            returns result
    """
    result = 0
    for i in list:
        result *= i
    return result
        
from createlist import *
from LoggingFile import *
logger  = func()
# Main Code
if __name__ == "__main__":
    list = create()
    result = mul(list)
    logger.info(f"\nThe multiplication of all elements of {list} is : {result}") 