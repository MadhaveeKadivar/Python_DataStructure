'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 14:59:11
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 14:59:11
    @Title : Add element in set
'''
if __name__=="__main__":
    num_of_values = int(input("\nEnter how many values you want to add in set : "))
    new_set = {input(f"\nEnter {i}th value : ") for i in range(num_of_values) }
    # for i in range(num_of_values):
    #     value = input(f"\nEnter {i}th value : ")
    #     new_set.add(value)
    print(f"Set : {new_set}")
    