'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 18:12:15
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 18:12:15
    @Title : Frozen set 
'''
from createSet import *
if __name__=="__main__":
    set_ele = create_set()
    print(f"\nSet : {set_ele}")
    print(f"\nMinimum element in {set_ele} : {min(set_ele)}")
    print(f"\nMaximum element in {set_ele} : {max(set_ele)}")