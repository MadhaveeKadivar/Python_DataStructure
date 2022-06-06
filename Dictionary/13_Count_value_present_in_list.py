'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 17:07:26
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 17:07:26
    @Title : Count numbers of value of dictionary that is list
'''
if __name__ == "__main__":
    dict_ele = {1 : ['a','b','c','d','e','f','g'], 2 : 'm', 3 : ['k','l'] }
    count = 0
    for x in dict_ele:
        if isinstance(dict_ele[x], list):
            count += len(dict_ele[x])
    print(f"\nTotal number of values in dictionary that are present in list : {count}")