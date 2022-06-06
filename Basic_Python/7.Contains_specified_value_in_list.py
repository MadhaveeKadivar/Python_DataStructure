'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 09:23:17
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 09:23:17
    @Title : Checking that specific value present in list or not 
'''
from LoggingFile import *
logger = func()
# Main Code
if __name__ == "__main__":

    no_of_elements = int(input("Enter how many numbers you want to add in list : "))
    list = [int(input(f"Enter {i+1} th value : ")) for i in range(no_of_elements)] 
    
    value = int(input("Enter value you want to check it is present in list or not : "))  
    if value in list:
        logger.info(f"{value} -> {list} : True")
    else:
        logger.info(f"{value} -> {list} : False")