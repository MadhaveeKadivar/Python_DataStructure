'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 13:47:31
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 13:47:31
    @Title : Unique values from Dictionary
'''
if __name__=="__main__":
    list_of_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    set_of_unique_value = {val for dic in list_of_dict for val in dic.values()}
    print(f"\nUnique values : {set_of_unique_value}")