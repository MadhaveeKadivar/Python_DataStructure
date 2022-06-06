'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 05:56:10
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 05:56:10
    @Title : Generate list and tuple from comma separated number string
'''
from LoggingFile import *
logger = func()
def generate_list(str):
    """ 
        Description: 
            This function is used for generating list
        Parameter:
            It takes two string argument one as user first name and second as user last name
        Return:
            returns list
    """
    list = str.split(",")
    return list
def generate_tuple(str):
    """ 
        Description: 
            This function is used for generating tuple
        Parameter:
            It takes two string argument one as user first name and second as user last name
        Return:
            returns tuple
    """
    tuple_result = tuple(str.split(","))
    return tuple_result

if __name__ == "__main__":
    str = input("Enter numbers seperated by comma : ")
    list = generate_list(str)
    logger.info(list)
    tuple = generate_tuple(str)
    logger.info(tuple)