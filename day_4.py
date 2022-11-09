Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 12
12
>>> # Indentation/Indent block
>>> print('hi')
hi
>>>  print('hi')# added extra space at start
SyntaxError: unexpected indent
>>> 100
100
>>>        300
SyntaxError: unexpected indent
>>> # Write a function to do the addition of 2 numbers
>>> def add():
	#indent
	print(10 + 20)

	
>>> add()
30
>>> def add():
	#indent
	print('Function')
print(10 + 20) #out of indentation
SyntaxError: invalid syntax
>>> def add():
	#indent
  print(10 + 20)

  
>>> add()
30
>>> def add():
	#indent
 print(10 + 20)

 
>>>  print(10)
SyntaxError: unexpected indent
>>> def add():
	#indent
print(10 + 20)
SyntaxError: expected an indented block
>>> # on shell we can do zigzag coding
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
30
>>> def add():
	#indent
    print('function')
print(10 + 20)
SyntaxError: invalid syntax
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
30
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
function
30
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
function
30
Yamen
>>> def add():
	#indent
    print('function')
add()
print(10 + 20)
def sample():
    print('Yamen')
sample()

SyntaxError: invalid syntax
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
function
30
Yamen
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
function
30
Yamen
>>> 
== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/fun.py ==
30
function
function
Yamen
>>> ################################
>>> # Literals in python
>>> a = 100
>>> # 100 is an int literal
>>> # literals are nothing but data types
>>> b = 'sample'
>>> # sample is a str literal
>>> 100
100
>>> 'sample'
'sample'
>>> 23.33 #float literal
23.33
>>> 3+4j # complex literal
(3+4j)
>>> # we identify objects with their data types and these data types are nothing but literals
>>> ####################################
>>> # print()
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> #print(value, ..., sep=' ', end='\n')
>>> # sep= 'space'
>>> print(10,20,30,40)
10 20 30 40
>>> # lets change sep
>>> print(10,20,30,40,sep = '--')
10--20--30--40
>>> print('Hi')
Hi
>>> print('Hi');print('Good evening')
Hi
Good evening
>>> print('Hi',end='\n\n');print('Good evening')
Hi

Good evening
>>> print('Hi',end=' ');print('Good evening')
Hi Good evening
>>> print('Hi',end=',');print('Good evening')
Hi,Good evening
>>> print('Hi',end=',');print('\nGood evening')
Hi,
Good evening
>>> # Use of escape sequences
>>> # \n: new line
>>> # \t: tab, 4 spaces
>>> print('Sampe file')
Sampe file
>>> print('Sample \nfile')
Sample 
file
>>> print('Sample \tfile') #4 space between 2 words
Sample 	file
>>> print('Sample \t\t\tfile') #4 space between 2 words
Sample 			file
>>> print(100)
100
>>> print(100,'hi')
100 hi
>>> print(100,'hi',sep='\n')
100
hi
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print(100)
100
>>> print(100,flush=True)
100
>>> 
