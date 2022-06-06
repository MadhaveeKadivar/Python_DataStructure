'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-16 06:41:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-16 06:41:07
    @Title : Calendar
'''
import calendar
from LoggingFile import *
logger = func()
# Main Code
if __name__ == "__main__":
    year = int(input("\nEnter year for which you want to get calendar : "))
    logger.info(calendar.calendar(year))
    # For particular month     
    year = int(input("\nEnter month for which you want to get calendar : "))
    month = int(input("\nEnter month number : "))
    logger.info(calendar.month(year, month))