'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 15:16:43
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 15:16:43
    @Title : Remove element in set
'''
from createSet import *
if __name__=="__main__":
    new_set = create_set()
    print(f"\nSet : {new_set}")
    remove_element = input("\nEnter element you want to remove from set : ")
    new_set.discard(remove_element)
    print(f"\nModified set : {new_set}")