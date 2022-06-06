'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 11:37:03
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 11:37:03
    @Title : Iterate over Dictionary
'''
if __name__=="__main__":

    no_of_pair=int(input("\nEnter how many pair you want to add in dict : "))
    dict_ele = {input(f"\nEnter {i}th key : "): input(f"\nEnter {i}th value : ") for i in range(no_of_pair)}

    # Iterate over for loop
    for key,value in dict_ele.items():
        print(f"\n{key} -> {value}")