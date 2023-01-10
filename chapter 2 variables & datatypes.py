# variables 
# Data types 
# Operators types 
# Type Function and Typecasting
# input function 
# practice set of chapter 2 





a = '''Hello 
world'''
b = 123
c = 4.4
d = True
f = False
e = None

'''
variables means a name of any contant like hello worlds name is a 

data types means 5 types 

string = str = 
Integer = int = non decimal numbers 
floting point numbers = decimals 
booleans = true/false, True = bytes, False = bool
None = to show as none


a is str
b is int
c is flot

'''

# reserved name or keyword = can't give thats name to any contanct

print(a)
print(b)
print(c)
print(d)
print(f)
print(e)

#to show type of variable = data types

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# 4 types of operators in python 
# Arithmetic, Assignment, comparison, Logical 

# Arithmetic Operators
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(4/2) #flotting numbers results, when / divide 


#assignment Operators, can add +, subtract-, divede/, multiple*
a = 10
a += 2
print(a)

A = 20
A -=10
A *= 2
A /= 4
print(A)


#Comparison Operators, value in True and False 
b = (1>2)
c = (1<2)
d = (1==2)
e = (1!=2)
f = (1<=2)

print(b)
print(c)
print(d)
print(e)
print(f)

print("Logical Operators")
#Logical Operators, and, or, not (Booleans)

bool1 = True 
bool2 = False
bool3 = True
bool4 = False


print("and logical operators")
# and 
print("true and false", (bool1 and bool2))
print("true and true = ",(bool1 and bool3))
print("false and false =",(bool2 and bool2))

print('or logical operators')
# or
print("true or false",(bool2 or bool1))
print("true or true",(bool1 or bool3))
print("false or false",(bool2 or bool4))



print("the value of bool1 and bool2 is", (bool1 and bool2))
print("the value of bool1 or bool2 is", (bool1 or bool2))
print("the value of not bool1 is", (not bool1))
print("the value of not bool2 is", (not bool2))


Bool6 = 1
Bool7 = 3 

print("the value of bool1 and bool2 is", (Bool6 and Bool7))
print("the value of bool1 or bool2 is", (Bool6 or Bool7))
print("the value of not bool1 is", (not Bool6))
print("the value of not bool2 is", (not Bool7))





# Type Function and Typecasting #

# type function is used to find data type of any variables 
# typecasting try to convert from one data type to another like.. int to str, str to int 

ab = 5 # types functin 
print(type(ab))

abc = str(ab) # typescasting
print(type(abc)) 

#str to int, if possible (means str value convertable)

a1 = "123"
print(type(a1))

a1 = int(ab)
print(type(a1))


#float to int

a2 = 1.20
print(type(a2))
print(a2)

a2 = int(a2)
print(type(a2))
print(a2)


#int to float

a3 = 22
print(type(a3))
print(a3)

a3 = float(a3)
print(type(a3))
print(a3)


#str to float
a4 = "30"
print(type(a4))
print(a4)

a4 = float(a4)
print(a4)
print(type(a4))

a5 = 20/2
print ("a5 is", print(a5), "and it's data types is", type(a5), "typecasting : ", "float to int", print(int(a5)))




### input function

# c = input("what is your name?")
# print("oh! your name is so good " + c)
# d = input(c + " what is your age by the way?")
# print("your age is",d,c)


#** input function always take answer in str formatin 




#//////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////




#********************** practice set of chapter 2 *************************#


'''
Q1 = write a program to add two numbers as variables
Q2 = write a program to add two numbers by input functin 
Q3 = write a program to get remainder when a no is diveded by another number
Q4 = write a program to find avg of two no entered by users



'''

#Q1 = add numbers as variables
e = 20 
f = 10
print("the addition of e and f is",(e+f))



#Q2 = add numbers by got input fucntion 
'''g = input('type any number: ')
h = input('type secound number :')
g = int(g)
h = int(h)
print('addition of that two numbers is',(g+h))
'''


#Q3 = remainder program 
i = 30
j = 4
print("remainder when", i, "divide", j ,"is", i%j )


#Q4 = write a program to find avg of two no entered by users
'''
k = input("enter number no 1 :")
l = input("enter a number no 2 :")
k = int(k)
l = int(l)
print((k+l)/2)
'''


