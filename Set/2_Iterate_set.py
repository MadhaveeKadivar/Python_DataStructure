'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 14:41:31
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 14:41:31
    @Title : Iteration of set
'''
if __name__=="__main__":
    string = input("\nEnter any string : ")
    new_set = set(string)
    print("\nIterate string using set : ")
    for i in new_set:
        print(i,end = " ")