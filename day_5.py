Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> id(10)
140735583016256
>>> a = 10
>>> id(a)
140735583016256
>>> b = 10
>>> id(b)
140735583016256
>>> # memory management is performed on head
>>> # heap
>>> a = 12.0
>>> id(a)
2695141307904
>>> b = 12.0
>>> b
12.0
>>> id(b)
2695141309440
>>> #real + img
>>> 3+4j
(3+4j)
>>> 0+0j
0j
>>> a = 3+4j
>>> id(a)
2695181501360
>>> b = 3+4j
>>> id(b)
2695181501392
>>> ##########################
>>> 12.0 is 12.0
True
>>> 12 == 12.0
True
>>> 12.0 == 12.0
True
>>> 12 isinstance 12.0
SyntaxError: invalid syntax
>>> 12 is 12.0
False
>>> id(12.0)
2695141309584
>>> id(12.0)
2695141309440
>>> id(12.0)
2695141309560
>>> 12.0 == 12.0
True
>>> 12.0 is 12.0
True
>>> a
(3+4j)
>>> a = 12.0
>>> b = 12.0
>>> a is b
False
>>> id(a)
2695141309584
>>> id(b)
2695141309464
>>> 12.0 is 12.0
True
>>> 12.0 == 12.0
True
>>> 12.12 == 12.123
False
>>> #Content equality and address equality
>>> 12' == 12.0
SyntaxError: EOL while scanning string literal
>>> 12 == 12.0
True
>>> 12 is 12.0
False
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
Enter age:12
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
Enter age:24
24
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
Enter age:'24'
Traceback (most recent call last):
  File "C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py", line 1, in <module>
    age = int(input('Enter age:'))
ValueError: invalid literal for int() with base 10: "'24'"
>>> # base 10 : [0-9]
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
Enter age:
Traceback (most recent call last):
  File "C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py", line 1, in <module>
    age = int(input('Enter age:'))
ValueError: invalid literal for int() with base 10: ''
>>> # int 32, float 64, complex 128
>>> import math
>>> c = 3+4j
>>> c.real
3.0
>>> c.img
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c.img
AttributeError: 'complex' object has no attribute 'img'
>>> c.imag
4.0
>>> ##############################
>>> keyword
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    keyword
NameError: name 'keyword' is not defined
>>> keyword.kwlist
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    keyword.kwlist
NameError: name 'keyword' is not defined
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import t
Enter age:23
23
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
Enter age:45
45
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
Enter age:2
2
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
False
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> import t
My name is Pallavi
>>> 
=== RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/t.py ===
ENter your age:
34
My name is Pallavi
>>> x = 4
>>> bool(x)
True
>>> bool(34)
True
>>> bool(-2)
True
>>> bool(0)
False
>>> bool(None)
False
>>> bool('')
False
>>> bool("")
False
>>> False
False
>>> bool('Manisha')
True
>>> bool(' ')
True
>>> 
