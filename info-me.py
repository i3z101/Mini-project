Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> def ali():
	name= input("name? ")

	
>>> ali()
name? abdulaziz
>>> def ali():
	name= input("name? ")
	print(name.upper())

	
>>> def ali():
	name= input("name? ")
	print(name.upper(1))

	
>>> ali()
name? abdulaziz
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ali()
  File "<pyshell#9>", line 3, in ali
    print(name.upper(1))
TypeError: upper() takes no arguments (1 given)
>>> def ali():
	name= input("name? ")
	print(name.upper())

	
>>> ali()
name? ali
ALI
>>> def ali():
	name= input("name? ")
	print(name[0].upper())

	
>>> ali()
name? aaaaaaa
A
>>> def ali():
	name= input("name? ")
	print(name[0].upper()+name[1])

	
>>> ali()
name? qaqsw
Qa
>>> def ali():
	name= input("name? ")
	print(name[0].upper()+name[1:])

	
>>> ali()
name? aknewiuricbjwer
Aknewiuricbjwer
>>> 
