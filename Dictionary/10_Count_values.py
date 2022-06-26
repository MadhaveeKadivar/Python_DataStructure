'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 14:05:42
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 14:05:42
    @Title : Count key value pair ocurrence from list of dictionary
'''
def count_value(list_of_dict,key,value):
    """ 
        Description: 
            This function is counting specific key values pair from list of dictionary
        Parameter:
            It takes list of dictionary ,key and value as argument
        Return:
            returns result 
    """
    result = 0
    for dict_ele in list_of_dict:
        for k,v in dict_ele.items():
            if str(k).lower() == key and str(dict_ele[k]).lower() == value:
                result += 1
    return result
    
if __name__=="__main__": 
    list_of_dict =  [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    key = input(f"\nEnter key : ")
    value = input(f"\nEnter value : ")
    result = count_value(list_of_dict,key.lower(),value.lower())
    print(f"\nNumbers of \"{key} : {value}\" present in list : {result}")
    