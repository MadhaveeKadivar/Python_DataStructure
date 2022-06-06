'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 17:45:04
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 17:45:04
    @Title : Clear set 
'''
from createSet import *
if __name__=="__main__":
    set_ele = create_set()
    print(f"\nBefore clearing, Set : {set_ele}")
    clear_set = set_ele.clear() # REmove all element from set 
    print(f"\nAfter clearing, Set : {set_ele}")
    