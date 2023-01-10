# 1. How to creat lists
# 2. list indexing 
# 3. change the value of list 
# 4. can creat different data types lists also 
# 5. Chaeck index of vary data types & List slicing 
# 6. change list value str
# 7. Chaneck data types using type function

# 8. List method  
# 9. Tuples 
# 10. Practice sets

#*****************************************************************


# 1 : How to creat lists
a = [1,3,5,7,9]

# 2 : list indexing
print(a[0])
print(a[0:])
print(a[:2])
print(a[::2])

# 3: change the value of list
a[0] = 20
print(a)

# 4 : can creat vary datatypes list also 
b = [12, "jaimin", False, True, 20.222]
print(b)

# 5 : chech the index value & List slicing 
print(b[0])
print(b[0:])
print(b[1])

# 6 : change list value of any str value
b[1] = "Hanumana"
print(b)

# 7 : Check data types using type fucntion 
print(type(b[0]))
print(type(b[1]))
print(type(b[2]))
print(type(b[3]))
print(type(b[4]))




#******************** 8 : List methods ***************************#

# in python there are many list method but very usefull type here below...
# sort, reverse, append, insert, pop, remove....etc.... len

c = [2,8,10,4,6,14,12]

# to know len of list
print(len(c))

#list sort method 
c.sort()
print(c)


#reverse method
c.reverse()
print(c)

c.reverse()

#append method
c.append(16)
c.append(18)
print(c)

# insert method = indexing used 
c.insert(0,0)
print(c)

c.insert(0,"Jaimin")
print(c)

c.insert(2,"Hanumana")
print(c)


# pop metheod = indexing used to remove
c.pop(0)
print(c)

# remove method = indexing not used, only value needed in ()
c.remove("Hanumana")
print(c)



# off topics = to know type 
print(c)
print(type(c))




#******************************** 9 : Tuples ***********************#
 
# to make tuples understand there are 3 types of tuples in python \
#empty tuples
d = ()
print(d)

# single element tuples
d = (20,)
print(d)

# more than one elements tuples 
d = (20,22,22,24)
print(d)


# to know the type
print(type(d))

# we can change the value in list but cannot in tuples usint indexing  
# list []
# tuples ()


# count function in tuples
print(d.count(22))

# index function in tuples  = to find index value of given () value or data 
print(d.index(24))

# add other data types in tuples
e = (20,22,"jaimin", False, 20.22)
print("jay hind")

print(e[0])

print(e)
print(type(e))

# tuples slicing
print(e[0:])
print(e[::2])


# to know the types of value using undexing 
print(type(e[0]))
print(type(e[1]))
print(type(e[2]))
print(type(e[3]))
print(type(e[4]))

# all same but we cannot update like list in tuples 
# like - change value, pop, append, sort, reverse, insert, remove, etc...
# so concution = tuples are immutable and list are mutable 
# immutable means = cannot changeble, and mutable meand = changeble 


#//////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////


#******************************** 10 : Pracatice sets ***************************#

# Q1 - write the python program to store seven fruits name in a list entered by users. 

'''
f1 = input("enter fruit no 1 : ")
f2 = input("enter fruit no 2 : ")
f3 = input("enter fruit no 3 : ")
f4 = input("enter fruit no 4 : ")
f5 = input("enter fruit no 5 : ")
f6 = input("enter fruit no 6 : ")
f7 = input("enter fruit no 7 : ")
fruit_list = [f1,f2,f3,f4,f5,f6,f7]
print(fruit_list)
'''

# Q2 - program to store student marks and display them in sort manner 

m1 = input("enter marks of student no 1 : ")
m2 = input("enter marks of student no 2 : ")
m3 = input("enter marks of student no 3 : ")
m4 = input("enter marks of student no 4 : ")
m5 = input("enter marks of student no 5 : ")
m6 = input("enter marks of student no 6 : ")
m7 = input("enter marks of student no 7 : ")


m1 = int(m1) 
m2 = int(m2)
m3 = int(m3) 
m4 = int(m4)
m5 = int(m5) 
m6 = int(m6)
m7 = int(m7)


mark_list = [m1,m2,m3,m4,m5,m6,m7]

mark_list.sort()
print(mark_list)

print(sum(mark_list))

# here sort work as alphabeticly because sort fucntion think these all value are string
# so you need to convert first str to int before sort it 


