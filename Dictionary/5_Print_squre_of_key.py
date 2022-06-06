'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 11:49:18
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 11:49:18
    @Title : Print square of key
'''
if __name__=="__main__":
    dict_ele = {}
    no_of_pair=int(input("\nEnter how many pair you want to add in dict : "))
    dict_ele = {i:i*i  for i in range(1,no_of_pair+1)}
    print(f"\nDictionary : {dict_ele}")
    
