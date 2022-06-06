'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 18:37:21
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 18:37:21
    @Title : Check element exist in tuple
'''

if __name__=="__main__":
    tuple_ele = ()
    no_of_elements = int(input("\nEnter how many numbers you want to add in tuple : "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i+1} th value : "))
        tuple_ele = tuple_ele + (number,)
    element = int(input("Enter which element you want to search : "))
    if element in tuple_ele:
        print(f"\n{element} is present in tuple {tuple_ele}")
    else:
        print(f"\n{element} is not present in tuple {tuple_ele}")