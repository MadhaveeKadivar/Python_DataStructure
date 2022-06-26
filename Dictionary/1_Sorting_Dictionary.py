'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 11:01:45
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 11:01:45
    @Title : Sorting dictionary 
'''


import operator
dict_ele = {1 : 2, 3 : 4, 4 : 3, 2 : 1, 0 : 0}
print(f"\nDictionary : {dict_ele}")
sorted_dict_asce_by_value = dict(sorted(dict_ele.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_dict_asce_by_value)
sorted_dict_desc_by_value = dict( sorted(dict_ele.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_dict_desc_by_value)

sorted_dict_asce_by_key = dict(sorted(dict_ele.items(), key=operator.itemgetter(0)))
print('Dictionary in ascending order by key : ',sorted_dict_asce_by_key)
sorted_dict_desc_by_key = dict( sorted(dict_ele.items(), key=operator.itemgetter(0),reverse=True))
print('Dictionary in descending order by key : ',sorted_dict_desc_by_key)