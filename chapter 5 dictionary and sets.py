# 1. intro of dictionary 
# 2. Dictionary methods
# 3. sets in python & methods
# 4. practice sets 




#********************************* 1 : intro of dictionary *************************#
# dictionary means collection of keys-value pairs

mydict = {
    "apple" : "it is a red colour fruit",
    "man" : "it's called human generic",
    "my marks" : [1,2,3,9,0],
    "anotherdic" : {"jaimin" : "developer",
     'hanumana' : 'the GURU of jaimin',
    
     'dic2' : {'hardi': 'the sister of jaimin',
         'bhavik' : 'jijaji of jaimin'
         } },

    29 : 200313101029


}


# we can also creat another dictionary in first dictionary 
# remember how to operate dictionary 
# remember how to operate dictionary in dictionary

print(mydict["apple"])
print(mydict["my marks"])
print(type(mydict["apple"]))
print(len(mydict["man"]))
print(type(mydict["my marks"]))

print(mydict["anotherdic"])
print(mydict["anotherdic"]["jaimin"])
print(mydict["anotherdic"]["hanumana"])

print(mydict["anotherdic"]["dic2"])
print(mydict["anotherdic"]['dic2']['hardi'])


#***************************************** 2 : Dictionary methods *********************************#
# 1. mydict.keys
# 2. mydict.values
# 3. items
# 4. update
    # method 1
    # method 2
# 5. get



print(mydict) # = to print full keys-value
print(mydict.keys()) # = to print only keys, dont forget ()
print(mydict.values()) # = to print only values, ()
print(mydict[29])


print(type(mydict))  # = <class 'dict'>
print(type(mydict.keys())) # = dict keys
print(type(mydict.values())) # = dict values
print(type(mydict[29]))  # int
print(type(mydict["anotherdic"])) # dict

print(list(mydict)) # same only keys
print(list(mydict.keys()))  # same only keys
print(list(mydict.values())) # show only values
print(list(mydict["anotherdic"])) # show only keys


# 3. items
print(mydict.items()) # show keys-values in tuples 


# 4. update
print("hello world")

print(mydict)

## method 1 
update_dict = {
    "love" : "feel good",
    "friend" : "feel nice"
}
mydict.update(update_dict)
print(mydict)

## Method 2
# update for more fast this is better than erlier method
mydict.update({"mom":"world","dad":"guid of world",20:200})
print(mydict)


# Method 3
more = {}
more00 = {}
more["none"] = "none00"
more[12] = 1200
more00[123] = 12300

print("more dict = \n", more)
print("more00 dict = \n",more00)



# also we can change value of old keys by update as new keys but keep old keys with new value.


# 5. get 
print(mydict.get('apple'))
print(mydict["apple"])
# both print value with two method but if you add wrong kets then
# .get function show NONE bcz it's tell us it is not in dictionary
# and mydict["apple0"] show error bcz it's show this is your responsibility to keep present

# print(mydict.get("apple0")) # - return none
# print(mydict["apple0"]) # - return error





#************************************* # 3. sets in python & methods *********************************#
# sets is a collection of non-repetitive elements

a = {1,2,3,4,50,1,2,30,20,33}
print(type(a))
print(a)

# diff between set, list, and tuples -----------------------------
print("dif between set, list, tuples")

# set = a = {1,2,3}
a = {1,10,12,21,100,22,'jaimin',False, 29.22}
print(type(a)) 
print(a)

# list = ab = [1,2,3,"jaimin"]
ab = [1,2,3,"jaimin", False, 29.22]
print(type(ab))
print(ab)

# tuples = abc = (1,2,3,"jaimin","hardi")
abc = (1,2,3,"jaimin", "hardi", False, 29.22)
print(type(abc))
print(abc)




# empty set, list, tuples and dict #** very important ----------------------------------

# = empty dict
a = {}
print(type(a))

# = empty tuples
ab = ()
print(type(ab))

# = empty list
abc = []
print(type(abc))

# = empty sets
abcd = set()
print(type(abcd))


# add method = how to add elements after creat empty sets ------------------------

abcd.add(2)
abcd.add(22)
abcd.add("jaimin")
abcd.add(False)
abcd.add(23.23)
# abcd.add({200,100,1000,"hardi",True}) # cant do like this = not add set in set
print(abcd)

 
# abcd.add([20,30,40,50]) # cant add list in sets
# print(abcd)

# abcd.add((20,30,40,"jaimin bariya")) # can add tuples in sets
# print(abcd)

# abcd.add({"jaimin":"the curious boy", 2:20}) # cannt add dict in sets 
# print(abcd)

# bcz list, sets, dict cnnt add in sets but tuples can 
# only can add hashable contant 




# sets methods in python 
# 1. len 
# 2. types
# 3. add
# 4. remove
# 5. pop
# 6. clear
# 7. union
# 8. intersection 



# len method = to knwo length 
print(len(abcd))

# 4. remove method = to remove
abcd.remove("jaimin")
print(abcd)

# 5. pop = ramdom
# 5 I - to remove first[0] 
# 5 II - to remove remove all remain first[0]

# 5 I - to remove first[0] 
# to remove random element = i think all time remove only first[0] element
abcd.pop()
print(abcd)

# 5 II - to remove remove all remain first[0]
# remove all without first[0]
print(abcd.pop())


# 6. clear = empties the set
abcd.clear()
print(abcd)

abcd.add(20)
print(abcd)

abcd.add(2220)
print(abcd)

print(abcd.add(32)) # show none

print(abcd)

print(abcd.clear()) # show none
print(abcd)


# 7 and 8. union and intersection in sets 

# set a1 and set a2 create

a1 = {1,2,20,3,4,4,3}
a2 = {1,22,24,200,299,4}

print(a1,a2)
# print(a2)

# a3 = a1.union(a2) same as a3 = a2.union(a1)
# print(a3)

a3 = a2.union(a1)
print(a3)

a4 = a1.intersection(a2)
print(a4)


#//////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////



#************************************** 4 : Practice sets ******************************#

#Q1 - write a program to create a hindi dictionary with the english translation and provide 
#keys to users to choose
'''
hindi_dict = {
    "pankha" : "fan",
    "osiku" : "pillow",
    "gulfi" : "candy"
        
}
print(hindi_dict.keys())
a = input("choose which word do you want to knoow?\n")
print("this is the english meaning of your entered word\n", hindi_dict.get(a))
'''

#Q2 - write a program to show 8 unique numbers entered from users 
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
print("sum of your no is", sum0)'''

#Q3 - create a dictionary. allow 4 friends to tell favourite language as value and keys their name and print.


'''
friend1 = input("what is your name1?\n")
lan1 = input("what is your favourite language1?\n")

friend2 = input("what is your name2?\n")
lan2 = input("what is your favourite language2?\n")

friend3 = input("what is your name3?\n")
lan3 = input("what is your favourite languag3?\n")

friend4 = input("what is your name4?\n")
lan4 = input("what is your favourite language4?\n")

pl = {
    friend1 : lan1,
    friend2 : lan2,
    friend3 : lan3,
    friend4 : lan4
    }
print(pl)
'''

#or method no 3 also can 

favlang = {}
favlang["raj"] = 12
print(favlang)

# note this - hashable means which cannot cahange in lifespan = set, tuples
# unhashable - dict, list 