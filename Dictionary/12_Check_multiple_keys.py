'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 18:47:12
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 18:47:12
    @Title : Check multiple keys 
'''
if __name__=="__main__": 
    dict_ele = {'name' : 'Madhavee' ,'color' : 'black' , 1 : 3  }
    multiple_keys_set = {'name', 1}
    multiple_keys_set2 = {'name','color','city'}
    all_keys_Set = set(dict_ele.keys())
    if multiple_keys_set2.issubset(all_keys_Set):
        print(f"\nAll the keys of {multiple_keys_set2} present in dictionary")
    else:
        print(f"\nNot all the keys of {multiple_keys_set2} present in dictionary")
    