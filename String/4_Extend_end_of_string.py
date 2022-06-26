'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 22:37:42
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 22:37:42
    @Title : Extend at end of string
'''
def extend_str(string):
    """ 
        Description: 
            This function is adding 'ing' to end of string if it is not ending with 'ing' else adding 'ly'
        Parameter:
            It takes one string as argument
        Return:
            returns modified string
    """
    length = len(string)
    if length >= 3:
        if string[-3:] == 'ing':
            string += 'ly'
        else:
            string += 'ing'
    return string
# Main Code
if __name__=="__main__":
    string = input("\nEnter any string : ")
    new_str = extend_str(string)
    print(f"\nModified string : {new_str}\n")
    