'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 22:45:31
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 22:45:31
    @Title : Longest word
'''
def find_longest(list):
    """ 
        Description: 
            This function is finding longest word from list
        Parameter:
            It takes one list of words as argument
        Return:
            returns longest word
    """
    longest = ''
    for i in list:
        if len(i) > len(longest):
            longest = i
    return longest

# Main Code
if __name__=="__main__":
    list = [] 
    no_of_elements = int(input("\nEnter how many element you want to add in list : "))
    for i in range(no_of_elements):
        value = input(f"\nEnter {i+1} th value : ")
        list.append(value)
    longest_word = find_longest(list)
    print(f"Longest word : {longest_word} and Length : {len(longest_word)}\n")