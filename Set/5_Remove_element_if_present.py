'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 15:37:12
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 15:37:12
    @Title : Remove element in set if it present
'''
from createSet import *
if __name__=="__main__":
    new_set = create_set()
    print(f"\nSet : {new_set}")
    remove_element = input("\nEnter element you want to remove from set : ")
    new_set.remove(remove_element)
    print(f"\nModified set : {new_set}")