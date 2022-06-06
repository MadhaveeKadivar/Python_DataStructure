'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 17:37:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 17:37:07
    @Title : Difference between two sets
'''
from createSet import *
if __name__=="__main__":
    set_1 = create_set()
    print(f"\nSet 1 : {set_1}")
    set_2 = create_set()
    print(f"\nSet 2 : {set_2}")
    # Difference set1-set2
    difference_set1 = set_1.difference(set_2) # Also work (set_1 - set_2)
    print(f"\nDifference of {set_1} and {set_2} is : {difference_set1}")
    # Difference set2-set1
    difference_set2 = set_2.difference(set_1) # Also work (set_1 - set_2)
    print(f"\nDifference of {set_2} and {set_1} is : {difference_set2}")
    