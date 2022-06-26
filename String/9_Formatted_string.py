'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 10:19:21
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 10:19:21
    @Title : Formatted string
'''

import textwrap
# Main Code
if __name__=="__main__":
    string = input("\nEnter any string: ")
    #print (string.center(50, '#'))
    #Enter any string: dfgh
    #######################dfgh#######################
    print()
    print(textwrap.fill(string, width=50)) 