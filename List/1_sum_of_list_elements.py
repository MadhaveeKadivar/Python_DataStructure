'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 10:35:09
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 10:35:09
    @Title : Sum of list element
'''
        
from createlist import *
from LoggingFile import *
logger  = func()
if __name__ == "__main__":
    list = create()
    total_sum = sum(list)
    logger.info(f"\nThe sum of all elements of {list} is : {total_sum}") 
