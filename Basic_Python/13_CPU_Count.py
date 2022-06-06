'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 10:35:59
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 10:35:59
    @Title : CPU Count
'''

import os
from LoggingFile import *
logger = func()
count = os.cpu_count()

logger.info(f"Number of CPUs in the system : {count}")