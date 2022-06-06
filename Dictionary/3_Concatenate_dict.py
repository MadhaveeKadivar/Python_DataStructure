'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 11:26:48
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 11:26:48
    @Title : Concatenate Dictionary
'''
if __name__=="__main__":
    dict_1 = {1:10, 2:20}
    dict_2 = {3:30, 4:40}
    dict_3 = {5:50,6:60}
    merge_dict = {**dict_1,**dict_2,**dict_3}
    print(f"\nMerge Dictionary : {merge_dict}")