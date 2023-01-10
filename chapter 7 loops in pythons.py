# note - loops helps when i want to repeat something or want to write in line or raw,
# for instance - print 1 to 1000
# loops make easy to tell to computer which things need to repeat and how many times 

# 1 - types of loops in python 
# 2 - while loop
# 3 - for loop
# 4 - function in for loops 
    # - range, 
    # - else 
    # - range function statements = break, continue, pass
# 5 - f string = print(f"{abc}X{i}={abc*i}") 
            # varibales in {} and go on 


####################################################################################################

#**************************** 1 - types of loops in python **********************************#
#primarily 2 types in python = 1. while loops and 2. for loops 



#***************************** 2 - while loops ************************************#

# syntax - 
'''

while condition :
        body of the loop 

note - if condition is true then body of the loops executed and again conditon will be check and 
body executed and this repeat untill condtion will be wrong or false


'''

# to print 1 to 50
a = 1
while a<=50:
    print(int(a))
    a = a+1


# to write jaimin 5 times with numbers

b = 1
while b<6:
    print("jaimin" , b)
    b = b+1

'''
c = 1
while c>0:
    print(int(c))
    c = c+1
'''

fruits = ["apple","banana","mangoes","watermelon"]
d = 0
while d<len(fruits):
    print(fruits[d])
    d = d + 1


#********************************************** 3 - for loops ***********************#

print("\nfor loop   \n")

for item in fruits:
    print(item)


# to print 1 to 10 in for loop
for i in range(11):
    print(i)

#note - by defult it start with 0 but if i want to start with 1 or 2 or 3 = use 1, or 2, or 3, 

for o in range(1,11):
    print(o)

#******************************************** # 4 - function in for loops *******************#
# 1 - Range funciton 

for z in range(1,21,2):
    print(z)
# here in range(start, stop, step-size)


#1 - the else 

for x in range(11):
    print(x)
else:
    print("done")


# =  else executed when full body end well 

#2 - the break statement 
for w in range(12):
    print(w)
    if w == 6:
        break


print("the continue statement")
#3 - the continue statement 

for v in range(10):
    if v == 6:
        continue
    print(v)
# 6 skipped 



print('the pass statement')
#4 - the pass statement 
u = [20.10,30,40,50,5,1]
u.sort()

for item in u:
    pass
print("done")


#//////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////


#1 = multiplication table 
'''
ab = int(input("enter table numbers"))
for ab in range(ab,ab*11,ab):
    print(ab)
'''


#or 

'''
abc = int(input("enter table no \n :"))
for i in range(1,11):
    # print(str(abc) + "X" + str(i) + "=" + str(i*abc))
    print(f"{abc}X{i}={abc*i}")
'''

'''
inp = int(input("enter the number here\n:"))
ab = 1
while ab*inp<=inp*10: # or # = while ab*inp<=inp*10:
    print(f"{inp} X {ab} = {inp*ab}")
    ab = ab + 1
print(f"table of {inp} is done")

'''



# Q2 - wap to greet whoes name start with j in l1 list

l1 = ["jaimin","raj","jatin","adit","jay"]
for name in l1:
    if name.startswith("j"):
        print("Good morening",name)


# Q3 - wap to find out whether a given no is prime or not


# num = int(input("enter the number \n:"))
# for i in range(2,num):
#     if (num%i==0):
#         print(str(num) + " is not prime no")
#     else:
#         print(str(num) + " is prime no ")

'''
num = int(input("enter number here\n:"))
prime = True
for i in range(2,num):
    if (num%i==0):
        prime = False
if prime:
    print(f"{num} is prime no")
else:
    print(f"{num} is not prime")
'''
'''
num1 = int(input("enter the no (solve using while loop\n:)"))
# prime1 = True
ab = 2
while num1%ab!=0:
    ab = ab + 1
    print("this is prime")
    break
else:
    print("this is not prime")

'''

# Q4 - wap to find a sum of n natural no using while loop in python 

'''
num0 = int(input("enter any numbers \n : "))
sum = 0
ab = 0
while ab<=num0:
    sum = sum + ab
    ab = ab + 1 
print(sum)

num1 = int(input("enter no to find factorial \n :"))
factorial = 1
for i in range(1,num1+1):
    factorial = factorial *i
print(factorial)

'''

print("jaimin "*4)
print("*"*0) 

# Q5 - print star* in n times 

# num = int(input('enter your n here\n :'))
# # by for loop 
# for i in range(1,num+1):
#     print("*"*(i))

ask = int(input("type any no \n :"))
for i in range(ask):
    print(" " * (ask-i-1),  end=" ")
    print("*" * (2*i+1), end=" ")
    print(" " * (ask-i-1))



