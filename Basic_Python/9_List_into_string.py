'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 09:56:42
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 09:56:42
    @Title : List into string
'''
from LoggingFile import *
logger = func()
if __name__ == "__main__":
 
    no_of_elements = int(input("Enter how many numbers you want to add in list : "))
    list = [int(input(f"Enter {i+1} th value : ")) for i in range(no_of_elements)] 
    str = ' '.join(list)
    logger.info(f"{list} into string : {str}")
    