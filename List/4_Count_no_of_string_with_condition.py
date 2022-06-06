'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 11:38:52
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 11:38:52
    @Title : Count string with condition from list
'''
def count_string(list):
    """ 
        Description: 
            This function is counting string based on condition from list
        Parameter:
            It takes list as argument
        Return:
            returns count
    """
    count = 0
    for i in list:
        if len(i) >= 2:
            if i[0] == i[-1]:
                count += 1
    return count

from createlist import *
from LoggingFile import *
logger  = func()
#Main Code
if __name__ == "__main__":
    list = create_string_list()
    count= count_string(list)
    logger.info(f"\nThe count of string having same first and last character and lenth is greater than 1 are : {count}") 