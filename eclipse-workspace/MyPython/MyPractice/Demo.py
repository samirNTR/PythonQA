'''
Created on 18-Dec-2023
@author: samir

'''
import keyword
testList=keyword.kwlist

print(testList)


print("First python program on eclipse")
 
username=10.444
print(username)
print(type(username))  #type function

x=600

print(x)
x=800
print(x)


name = "Bob"
age = 25
print("Name: {}, Age: {}".format(name, age)) #1 print stattement

name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}") #2 approach


# In Python, str() is a built-in function used to convert a value into a string.
name = "Charlie"
age = 35
print("Name: " + name + ", Age: " + str(age)) #3 approach


name="Kutta"
age=89
print("Name:{}, Age is:{}".format(name,age))

name='oolalala'
age=98

print(F"Name is:{name}, Age is:{age}")


x=900
print(x)
y=x
print(y)
print(id(y)) # print the id memory location
print(id(x))

age=99
print("Name:{}" , "Age:{}".format(name,age))
print(f"Name:{name},Age:{age}")


# Using concatenation to print in a single line
print("This is printed ", end="")
print("on the same line.")

# Using formatted strings (f-strings) to print in a single line
value = 42

#Single Line print
print(f"The value is: {value}", end=", ")
print("and this is printed on the same line.")
myList=keyword.iskeyword("try")
print(myList)

############################################
####OPERATORS######
a=15
b=4

print(a*b)
print(a%b)
print(a-b)
print(a/b)
print(a**b) #15^4
print(a//b)

x=["kutta","kutta"]
y=["kutta","kutta"]
print(x ==y)
print(x is y)
####Membership Operators###
print("kutta" in x)
print("kutta" not in x)



