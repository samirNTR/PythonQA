import string

#Both quotes are accepted
x="I love python"
y='I love python'


a="I  'love' python very much"

b='I  "love" python very much'
c="I  \'love\' python very much"  #Escape sequence

print("This is " +a)
print(b)
print(c)
print(x)
print(y)

#As array

print(x[2])
print(y[9])

#Using strings to define multiline comments

z="""
This is multiline string                '
"""

c='''
This is also a multiline string
'''

print(z)
print(c)
#Membership operator in string

print("iss" in c)