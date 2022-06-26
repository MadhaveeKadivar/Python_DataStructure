'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 10:59:17
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 10:59:17
    @Title : Lower case upto specific index
'''
# Main Code
if __name__=="__main__":
    string = input("\nEnter any string: ")
    index = int(input("Enter specific index : "))
    if index > len(string):
        print(f"\nEnter index value within 0 to {len(string)}")
    else:
        new_str = string[:index].lower()+string[index:]
        print(f"\nString in lower case upto {index}th index : {new_str}")