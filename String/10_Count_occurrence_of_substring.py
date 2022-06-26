'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 10:38:34
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 10:38:34
    @Title : Count occurrence of substring in string
'''
# Main Code
if __name__=="__main__":
    string = input("\nEnter any string: ")
    sub_string = input("\nEnter any sub string: ")
    string_lower = string.lower()
    substr_count = string_lower.count(sub_string.lower())
    print(f"Total occurrence of \"{sub_string} in \"{string}\"  :  {substr_count}")