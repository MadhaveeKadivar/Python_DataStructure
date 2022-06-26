'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 18:30:51
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 18:30:51
    @Title : Print dict in table format
'''
if __name__=="__main__": 
    num_list = [1, 2, 3, 4]
    new_dict = current = {}
    for name in num_list: 
        current[name] = {}
        print(current)
        current = current[name]                     
    print(new_dict)