# 1 - intro to if-elif-else 
# 2 - small quiz 
# 3 - relational operators (comparison )
# 4 - logical operators
# 5 - in and is



#**************************** 1 - intro to if-elif-else ********************#

# if use when one sitution depend on other means if rain stop then you will go to your office 
# elif - means = first if condition not work then next elif comes in lightspot
# we can creat multiple elif condtion 
# at last, else comes - if both if and elif wrong then else happens 

#syntax of if-elif-else 

a = 20
if (a>21):
    print("yes,", a, "is greater than 10")
elif(a>23):
    print("yes, 20 is greater than 10")
else:
    print("bye, tata")



#************************************** 2 - small quiz  *****************************#

# Q = write a program while user input is greater than or equal to 18 then print yes, otherwise no.
'''
ans = int(input("enter you age :"))
if(ans>=18):
    print("Yes")
else:
    print("NO")
'''



'''

n1 = int(input("enter your no 1\t"))
n2 = int(input("enter your no 2\t"))
n3 = int(input("enter your no 3\t"))
n4 = int(input("enter your no 4\t"))
n5 = int(input("enter your no 5\t"))
n6 = int(input("enter your no 6\t"))
n7 = int(input("enter your no 7\t"))
n8 = int(input("enter your no 8\t"))

a1_8 = {n1,n2,n3,n4,n5,n6,n7,n8}
print("this is the unique no you entered\n = ",a1_8)
sum0 = sum(a1_8)

inpot = input("if you want to sum of this no type yes otherwise type no\n:")

if(inpot=="yes"):
    print("sum of your no is", sum0)
else:
    print("okay!, thank you very much")


'''


#*********************************** 3 - relational operators ****************************#

# : == equals
# : >= greater thann euqal
# : < less than euqal
# : > 
# : <


#*********************************** 4 - logical operators ********************************#

# 1 : and = true if both statements are work 
# 2 : or = true if any one of both statements are work 
# 3 = not = invert - true to false and false to true 
            # not true = false, not false = true 


#********************************* 5 - in and is **********************************#

# is 
a = None
if (a is None):
    print("yes")
else:
    print("no!")


# in
a = [1,2,3.3,50,"jaimin"]
print(1 in a)
print(3.3 in a)
print("jaimin" in a )
print("hardi" in a )
print(22 in a)

# so in gives answer in booleans 



#//////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////


# Q1 - wrtie a program to print greatest number among 4 numbers entered by users
'''
num1 = int(input("write no 1 : "))
num2 = int(input("write no 2 : "))
num3 = int(input("write no 3 : "))
num4 = int(input("write no 4 : "))

if(num1>num2):
    f1 = num1
else:
    f1 = num2

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print("the greatest number is", f1)
else:
    print("the greatest number is", f2)

'''
# here in this expample you learned how to use 'pass'

# Q2 - write a program to find out student is pass or fail, if 40% in total and 33% in each subject require to pass
# 3 sub marks entered by users
'''
sub1 = int(input("enter 1st sub marks\n:"))
sub2 = int(input("enter 2st sub marks\n:"))
sub3 = int(input("enter 3st sub marks\n:"))

if(sub1>=33 and sub2>=33 and sub3>=33 and (sub1+sub2+sub3)/3>=40):
    print("congo, you are pass!")
else:
    print("sorry, you are fail")

'''


# Q3 - wap to find out email is spam or not if email contaning this word 
# - "make a lot of money"
# - "buy now"
# - "subscribe this"
# - "click this"

'''text = input("enter your text here:\n")'''

'''

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam==True): # also "if(spam):" work  
    print("this is spam")
else:
    print("this is not spam")

   ''' 


'''
if("buy now" in text or "make a lot of money" in text or "click this" in text or "subscribe this" in text):
    print("this is spam")
else:
    print("this is not spam")
'''


# Q4 - write a program to find out username entered by use is less than or equal to 10 character or not
'''
enter = input("enter user name here:\n")
enter_len = len(enter)

if(enter_len<=10):
    print("pass")
else:
    print("fall")

'''


# Q5 - write a program to find out name is present in list or note

'''am = ["a","b","c","d","e","f"]
enter = input("write your name, we will check your name is in your name or not:\n")

if(enter in am):
    print("yes, you are allow")
else:
    print("sorry, you are not allow")
'''


# Q6 - wap to give gread to student by enter marks by user 
'''
90 - 100 = ex
80 - 89 = A
70 -79 = B
60 - 69 = c
50 - 59 = d
<50 = f
'''

'''enter = input("enter your name here \n : ")
enter_marks = int(input("enter your marks here \n : "))
'''

'''
if(enter_marks>=90 and enter_marks<=100):
    print(enter,"your gread is - EX")
elif(enter_marks>=80 and enter_marks<90):
    print(enter, "your gread is - A" )
elif(enter_marks>=70 and enter_marks<80):
    print(enter, "your gread is - B" )
elif(enter_marks>=60 and enter_marks<70):
    print(enter, "your gread is - C" )
elif(enter_marks>=50 and enter_marks<60):
    print(enter, "your gread is - D" )
else:
    print("F")


'''

# or
'''
if enter_marks>=90:
    print('EX')
elif enter_marks>=80:
    print("A")
elif enter_marks>=70:
    print("B")
elif enter_marks>=60:
    print("C")
elif enter_marks>=50:
    print("D")
elif enter_marks<50:
    print("F")
'''



# Q7 - wap to find out a word "jaimin" used in post or not (post means text) 
'''
text = input("type your text here \n : ")
textt = text.upper()
if("JAIMIN" in textt):
    print("yes, mentioned")
else:
    print("not, mentioned")
'''


