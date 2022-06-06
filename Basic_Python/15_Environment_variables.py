'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 10:57:11
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 10:57:11
    @Title : Access Environment variable
'''

import os
from LoggingFile import *
logger = func()
logger.info(os.environ)
logger.info("\n")
homepath = os.getenv('HOMEPATH')
logger.info(f"Homepath : {homepath}")
os_name = os.environ.get('OS')
logger.info(f"OS Name : {os_name}")