'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 10:03:13
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 10:03:13
    @Title : String before specified character
'''
if __name__=="__main__":
    string = input("\nEnter any string: ")
    char = input("\nEnter any specific character : ")
    char_index = string.index(char)
    new_str = string[0:char_index]
    print(f"\nString before \"{char}\" : {new_str}")
    