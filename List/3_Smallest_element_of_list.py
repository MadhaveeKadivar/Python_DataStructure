'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 11:19:52
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 11:19:52
    @Title : Smallest element of list
'''
        
from createlist import *
from LoggingFile import *
logger  = func()
if __name__ == "__main__":
    list = create()
    smallest= min(list)
    logger.info(f"\nThe Smallest element of all elements of {list} is : {smallest}") 