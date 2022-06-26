'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 18:44:27
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 18:44:27
    @Title : List to tuple
'''
if __name__=="__main__":
    list = [] 
    no_of_elements = int(input("\nEnter how many numbers you want to add in list : "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i+1} th value : "))
        list.append(number)
    print(f"\nList : {list}")
    print(f"\nTuple : {tuple(list)}") # Converting list to tuple