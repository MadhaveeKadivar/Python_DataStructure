'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 11:13:34
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 11:13:34
    @Title : Add value to dictionary 
'''

if __name__=="__main__":
    no_of_pair=int(input("\nEnter how many pair you want to add in dict : "))
    dict_ele = {input(f"\nEnter {i}th key : "): input(f"\nEnter {i}th value : ") for i in range(no_of_pair)}
    # for i in range(no_of_pair):
    #     key = input(f"\nEnter {i}th key : ")
    #     value = input(f"\nEnter {i}th value : ")
    #     dict_ele[key] = value
    print(f"\nDictionary is : {dict_ele}")
    # Add value in dict
    dict_ele[2] = 30
    dict_ele['name'] = 'Madhavee'
    print(f"\nDictionary is : {dict_ele}")