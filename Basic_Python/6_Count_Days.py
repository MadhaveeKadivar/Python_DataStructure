'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 06:59:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 06:59:07
    @Title : Count days between two days
'''

from datetime import date
from LoggingFile import *
logger = func()
 
def days(date1, date2):
    """ 
        Description: 
            This function is used for counting days between two dates
        Parameter:
            It takes two date as argument
        Return:
            returns days
    """
    result=date2-date1
    num_of_days = result.days
    return num_of_days
     
# Main Code
if __name__ == "__main__":
    date1 = date(2014, 7, 2)
    date2 = date(2014, 7, 11)
    days_count = days(date1, date2)
    logger.info(f"Days between {date1} and {date2} are : {days_count}")
    