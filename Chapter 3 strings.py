# 1. Intro to Strings 
# 2. String Indexing 
# 3. String slicing 
# 4. String Function 
# 5. Escape Sequence Characters
# 6. Practice set



#************************* 1 : Intro to Strings *****************************#
# strings is a sequence of characteres inclosed in quote can be single, double and triple also.



a = "30"
b = "Jaimin"
c = 'jaimin1'
d = '''jaimin 2 and 
jaimin 3'''

print(a,b,c,d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#***

print("'jaimin'")
print('"jaimin"')
print('''"'jaimin'"''')



#****************************** 2. String Indexing **************************#

A = "jaimin"
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
print(A[5])

print('Hello world')

print(A[-1])
print(A[-2])
print(A[-3])
print(A[-4])
print(A[-5])
print(A[-6])


print('Hello World')

'''
name = input('what is your name?')
greeting = 'Good Morning, '
A = greeting + name #Concatenating two strings
print(A)
'''

#****************************** 3. String slicing *************************#

name = "JaiminBariya"
print(name[5])
print(name[6])


print(name[0:3]) #count only o,1,2
print(name[4:6]) # count only 4,5
print(name[:3]) # count 0,1,2 , space same as 0 but here first 3 count

print('hello world')

print(name[0:]) # 0 counted and 0 to till end 
print(name[1:]) # start with 1 and till end
print(name[2:]) # start with 2 and till end 


'''
note : 

print(name[x:y])
x = counted 
y = not counted 

print(name[:y])
first y counted

print(name[0:])
0 to till end of variable

'''


# slicing with skip value 
print('slicing with skip')

name = "JaiminAndHanuman"
print(name[0::1])

print('hello world')

print(name[1::2])




#******************************** 4. String function *************************#
print('''
    string function

    
    ''')

story = "once upon a time there lived a ghost"

#no 1 = length Function = to count length 
print(len(story))


#no 2 = endwith function = to find last word or character end with this or not
# = give answer in booleans = true and false
print(story.endswith("ghost"))
print(story.endswith("gho"))
print(story.endswith("t"))

#no 3 = count function = to count any character or word in string 
print(story.count("a"))
print(story.count("time"))

#no 4 = capitalize function = used to convert first character in capitalize 
print(story.capitalize())

#no 5 = find function = to find any character or word = answer in index value of string
print(story.find("upon")) #means upon start at 5 index value
print(story.find("u"))
print(story.find("upn")) #if any word or character not exist in string thaen answer is = -1


#no 6 = Replace function = to replace any word or character in string
print(story.replace("a","an"))



#***************** 5. Escape Sequence Characters ********************#
# \n = for new line
# \t = for a tab
# \' = for single quote
# \\ = for one backslash
# etc...


story = "Jaimin \nis the student of Hanumana"
print(story)

story1 = "Jaimin is the \tstudent of Hanumana"
print(story1)

story2 = "Jaimin \t\tis the student of Hanumana"
print(story2)

story3 = "Jaimin is the student\' of Hanumana"
print(story3)

story5 = "Jaimin is the student' of Hanumana"
print(story5)

story4 = "Jaimin is \\the student of Hanumana"
print(story4)




#//////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////



#************************* 6. Practice set *********************#
print('''   

''')

# Q1 = Name + Good afternoon program 

# greeting = "Good afternoon "
# name = input("what is your good name?")
# A1 = greeting + name
# print(A1)


# Q2 = add input person name and date

letter = '''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''



name = input("what is your good name?\n")
date = input("enter today's date below\n")
letter0 = letter.replace("<|NAME|>", name) 
letter1 = letter0.replace("<|DATE|>", date)

print("\n",letter1)




