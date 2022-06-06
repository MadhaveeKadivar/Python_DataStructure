'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 17:53:22
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 17:53:22
    @Title : Frozen set 
'''

if __name__=="__main__":
    
    tuple_ele = ('a',"Hello",5)
    dict_ele = {"name": "Madhavee", "age": 23}
    frozen_set_tuple = frozenset(tuple_ele)
    frozen_set_dict = frozenset(dict_ele)
    print(f"\nThe frozen set for tuple is : {frozen_set_tuple}")
    print(f"\nThe frozen set for dictionary is : {frozen_set_dict}")
    print(f"\nThe empty frozen set : {frozenset()}")

    # frozensets are immutable
    # frozen_set.add('v') --> Throw error