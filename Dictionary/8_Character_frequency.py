'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-19 13:08:46
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-19 13:08:46
    @Title : Character frequency 
'''
if __name__=="__main__": 
    string = input("\nEnter a string: ")
    char_freq_of_dict = { char : string.count(char) for char in string }
    # for ch in string:
    #     if ch in char_freq_of_dict : 
    #         char_freq_of_dict[ch] += 1
    #     else:
    #         char_freq_of_dict[ch] = 1 
    print(f"\nCharacter frequency : {char_freq_of_dict}")