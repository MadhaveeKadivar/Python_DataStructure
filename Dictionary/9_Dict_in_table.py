'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 13:22:24
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 13:22:24
    @Title : Print dict in table format
'''
if __name__=="__main__": 
   
    no_of_pair=int(input("\nEnter how many pair you want to add in dict : "))
    dict_ele = {input(f"\nEnter {i}th key : "): input(f"\nEnter {i}th value : ") for i in range(no_of_pair)}
    keys_ele = dict_ele.keys()
    value_ele = dict_ele.values() 
    for each_row in zip(keys_ele,value_ele):
        print(*each_row, " ")
