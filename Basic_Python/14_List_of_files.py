'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 10:46:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 10:46:01
    @Title : List of Files
'''
import os
from LoggingFile import *
logger = func()
path = "D:\Python_ML_Bridgelabz\Python_DataStructure\Basic_Python"
dir_list = os.listdir(path)
 
logger.info("List of files and directories in '", path, "' : \n")
logger.info(dir_list)
logger.info()