'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 10:21:33
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 10:21:33
    @Title : File Exists or not
'''
import os.path
from os import path
from LoggingFile import *
logger = func()
def file_exists(filename):
    """ 
        Description: 
            This function is used to check file is exists or not
        Parameter:
            It takes file name
        Return:
            returns True or False
    """
    if path.exists(filename):
        return True
    else:
        return False
    
# Main Code
if __name__== "__main__":
    filename = input("\nEnter only file name if you want to check in pwd otherwise enter path with filename : ")
    result = file_exists(filename)
    logger.info(f"File exists : {result}")