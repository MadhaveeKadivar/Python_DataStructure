'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 06:14:23
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 06:14:23
    @Title : Getting First and Last element of string
'''
from LoggingFile import *
logger = func()
if __name__ == "__main__":
    color_list = ["Red","Green","White" ,"Black"]
    logger.info(f"First color : {color_list[0]}")
    logger.info(f"Last color_: {color_list[-1]}")
    logger.info(color_list[::len(color_list)-1])