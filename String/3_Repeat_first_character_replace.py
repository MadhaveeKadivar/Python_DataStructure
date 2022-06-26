'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 22:23:20
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 22:23:20
    @Title : Repeat first character replace 
'''
def replace(string):
    """ 
        Description: 
            This function is replacing all occurrence of first character with $ except first ocurrence
        Parameter:
            It takes one string as argument
        Return:
            returns modified string
    """
    new_str = string[0]
    for i in range(1,len(string)):
        if string[i] == string[0]:
            new_str += '$'
        else:
            new_str += string[i]            
    return new_str
        
# Main Code           
if __name__=="__main__":
    string = input("\nEnter any string : ")
    new_str = replace(string)
    print("\nModified string : ")
    print(new_str)
  