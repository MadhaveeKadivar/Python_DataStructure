'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 18:16:58
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 18:16:58
    @Title : Unpack tuple to variable
'''
if __name__=="__main__":
    tuple_ele = (1,2,"Hii",2.3)
    var1,var2,var3,var4=tuple_ele # Unpacking tuple element in variable
    print(f"\nTuple with different data types element : {tuple_ele}")
    print(f" Element 1 : {var1} \n Element 2 : {var2} \n Element 3 : {var3} \n Element 4 : {var4}")