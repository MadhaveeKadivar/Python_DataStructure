'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 09:39:25
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 09:39:25
    @Title : Sorting words
'''
def sort_str(string):
    list_ele = string.split(",")
    sorted_list = sorted(list(set(list_ele)))
    new_str = ",".join(sorted_list)
    return new_str
# Main Code
if __name__=="__main__":
    string = input("\nEnter any comma seperated value : ")
    new_str = sort_str(string)
    print(f"\nAfter soring string is : {new_str}\n")

