
#----> swapping of variables
"""
a = 7
b = 5

temp = a
a=b
b=temp
#here we can take any word or letter in temp variable place
print(a,b)
#Eg : 2
a=b+2
b=a-b
a=a-b
print(a,b)
"""
"""
a,b=b,a #only in use in python
print(a,b)
"""

"""
a=2
b=4
a=a*b
b=a/b
a=a/b
print(a,b)#the ouput for this in decimals
#for not get in decimal form put int in the side of a and b
# for example print(int(a),int(b))
"""
"""
a=7
print(a)
print( id(a))
#id function used to find the memory adress of variable 
"""
"""
#----> keywords
#keywords or resevered words which provides special meaning to
#compilers or interpretor
import keyword
print (keyword.kwlist)

print(len(keyword.kwlist))
print(type(keyword.kwlist))
"""
"""
#to check the string is keyword or not
print(keyword.iskeyword("smd"))
if = 8
print(if) #error coz if is a keyword
"""
"""
#!-->literals
#literals is the constant value assigned to a variable
#a variable is considers to be constant when it is defines
#in caps
a=75 #a is variable
A=75 #A is a constant
"""

"""
#hash()---> it creares a hash value for constant datatypes and
#provides error for non  constant data types
n1 = 89+7j
print(hash(n1))

f1 = [ 7,8,9]
print(hash(f1)) #error---> list is non-constant or mutable datatype
"""

#!---->operators
#operators are symbols which is used to perform various operations
# b/w 2mor more operands
"""
 -Types of operators(7)
 Arithmatic
 Assignment
 Logical
 Relational or comparison
 Bitwise
 Identify
 Membership
 """

"""
# --->Arithmatic --> +,-,*,/,%,//,**
 Eg:1
 a=3
 b=8
 c=3
 print(a+b+C)

#input()--> used to get the runtime input
 n1 = input("Enter the value:")
 print(type(n1))
 
#eval()--> used to get the runtime values of all  the datatypes
 n1 = eval(input("Enter the value:"))
 print(type(n1))
"""
"""
 a = 4
 b = 2
 print(a/b) # is used to get the quatient value
 print(a%b) # is used to get the remainder value
# ! // ---> floor division
a= 3432
b=12
print(a//b) #->the output will be in interger & the output will be
# based on floor
"""
"""
#! ** -->
print(2**4) # 16 ANSWERS
"""

# s1 = int(input("Enter the number :"))
# if s1%2==0:
#    print(s1,"yes")
# else:
#     print(s1,"no")
"""
m = str((input("Enter the Name :")))
n = str((input("Enter the Nationality :")))

    
t = int(input("Enter the Age :"))
if t >18 and n== "indian":
    print("Eligible")
else:
    print("Not Eligible")
"""

a = 10
b = 3
print(a/b) # is used to get the quatient value



