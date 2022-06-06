'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 12:32:55
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 12:32:55
    @Title : Remove key from Dictionary
'''
if __name__=="__main__":

    no_of_pair=int(input("\nEnter how many pair you want to add in dict : "))
    dict_ele = {input(f"\nEnter {i}th key : "): input(f"\nEnter {i}th value : ") for i in range(no_of_pair)}
    print(f"\nDictionary is : {dict_ele}")
    ele = input(f"\nEnter key which you want to remove from dictionary : ")
    del dict_ele[ele]
    print(f"\nModified Dictionary is : {dict_ele}")
        