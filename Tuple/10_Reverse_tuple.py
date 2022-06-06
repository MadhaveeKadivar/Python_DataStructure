'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 20:02:44
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 20:02:44
    @Title : Tuple in reverse order
'''
if __name__=="__main__":
    tuple_ele = ()
    no_of_elements = int(input("\nEnter how many numbers you want to add in tuple : "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i+1} th value : "))
        tuple_ele = tuple_ele + (number,)
    print(f"\nTuple : {tuple_ele}")
    print(f"\nTuple in reverse order : {tuple_ele[::-1]}\n")