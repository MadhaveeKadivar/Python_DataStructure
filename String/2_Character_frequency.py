'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 22:12:57
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 22:12:57
    @Title : Character Frequency
'''
def frequency(string):
    """ 
        Description: 
            This function is calculating character frequency of string
        Parameter:
            It takes one string as argument
        Return:
            returns dictionary of character frequency
    """
    char_freq = {} 
    for i in string:
        if i in char_freq:
            char_freq[i] += 1
        else:
            char_freq[i] = 1
    return char_freq

if __name__=="__main__":
    string = input("\nEnter any string : ")
    char_freq = frequency(string)
    print("\nThe frequency of all characters in \"{string}\" are : ")
    print(char_freq)
    print()
