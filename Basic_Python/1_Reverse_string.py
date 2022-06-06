'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 05:40:51
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 05:40:51
    @Title : Reverse String
'''
from LoggingFile import *
logger = func()
def name_reverse(first_name,last_name):
    """ 
        Description: 
            This function is used for reversing user first name and last name
        Parameter:
            It takes two string argument one as user first name and second as user last name
        Return:
            returns reverse string
    """
    return f"{last_name} {first_name}"
# Main Code
if __name__ == "__main__":
    first_name = input("Enter first name : ")
    last_name = input("Enter last name : ")  
    str = name_reverse(first_name,last_name)
    logger.info(str)