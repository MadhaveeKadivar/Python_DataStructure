'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 09:45:53
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 09:45:53
    @Title : Histogram
'''
from LoggingFile import *
logger = func()
# Main Code
if __name__ == "__main__":

    no_of_elements = int(input("Enter how many numbers you want to add in list : "))
    list = [int(input(f"Enter {i+1} th value : ")) for i in range(no_of_elements)] 
    logger.info(f"\nHistogram of {list} :\n")
    for i in list:
        print("*"*i,end="\n")
        