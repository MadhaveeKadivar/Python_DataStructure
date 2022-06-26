'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 15:49:46
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 15:49:46
    @Title : Intersection of two sets
'''
from createSet import *
if __name__=="__main__":
    set_1 = create_set()
    print(f"\nSet 1 : {set_1}")
    set_2 = create_set()
    print(f"Set 2 : {set_2}")
    # Intersection  ... Also work (set_1 & set_2 )
    intersect_set = set_1.intersection(set_2) 
    print(f"\nIntersection of {set_1} and {set_2} is : {intersect_set}")
