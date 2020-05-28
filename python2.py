Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> # print is a buildin function in python , Hello World is a argument or string argument
>>> print(25)
25
>>> print(50*60)
3000
>>> print("50*10=" 50*10)
SyntaxError: invalid syntax
>>> print("50*10=", 50*10)
50*10= 500
>>> print("Hello" , " " , " World")
Hello    World
>>> x=50
>>> y=10
>>> print("{0}*{1} = {2}".format(x,y,x*y))
50*10 = 500
>>> x=40
>>> y=10
>>> print("{0}+{1} = {2}".format(x,y,x+y))
40+10 = 50
>>> print("{0}*{1} = {2}".format(x,y,x+y))
40*10 = 50
>>> print("{0}+{1} = {2}".format(x,y,x*y))
40+10 = 400
>>> print("Hello" ,"World" , sep="----------")
Hello----------World
>>> #C style formatted string
>>> name="Max"
>>> print("Hello %s" % name)
Hello Max
>>> age=22
>>> print("Hello &s ! are you %d years old" %(name , age))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("Hello &s ! are you %d years old" %(name , age))
TypeError: %d format: a number is required, not str
>>> age=22
>>> print("Hello %s ! are you %d years old" % (name , age))
Hello Max ! are you 22 years old
>>> print("marks = %f" %92.5)
marks = 92.500000
>>> print("marks = %.2f" %92.5)
marks = 92.50
>>> print("marks = %.4f" %92.5)
marks = 92.5000
>>> value = input("Enter some value")
Enter some value 50
>>> value
' 50'
>>> type(value)
<class 'str'>
>>> value = int(input("Enter some value"))
Enter some value50
>>> value
50
>>> value = float(input("Enter some value"))
Enter some value100
>>> value
100.0
>>> 