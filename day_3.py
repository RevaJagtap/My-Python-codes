Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Identity operator
>>> # it check identity of an object
>>> # it will check wither 2 objects are equal or not
>>> # is , is not
>>> # compares 2 object
>>> 12 is 12
True
>>> 12 is 12.0
False
>>> 'python' is 'python'
True
>>> # if both the objects are same
>>> # same means id's are same
>>> # if ids are same  then 2 objects are identical
>>> id(12)
140735576659328
>>> id(12.0)
2102979836928
>>> # hence we have different ids for 12 and 12.0 thats why it gives False
>>> 12 is not 12.0
True
>>> id(12.0)
2102979836952
>>> id(12.0)
2102979835392
>>> f = 3.2
>>> id(f)
2102979836880
>>> id(3.2)
2102979837072
>>> id(f)
2102979836880
>>> c = 3.2
>>> id(c)
2102979837072
>>> d = 3.2
>>> id(d)
2102979836928
>>> id(12)
140735576659328
>>> 50
50
>>> id(50)
140735576660544
>>> x = 50
>>> id(x)
140735576660544
>>> ##############################
>>> # interview question
>>> 12 ==  12
True
>>> 12 == 12.0
True
>>> 12 is 12
True
>>> 12 is 12.0
False
>>> # Content equality and address equality
>>> # when we use == it checks contents
>>> # when we use is, it checks address/id
>>> ########################################
>>> # Logical operator: and , or , not
>>> # here we check conditions
>>> # its conditional base, retursn boolean output
>>> # Foundation for this is Truth table
>>> # False= 0 and True=1
>>> 0 and 0
0
>>> 0  and 1
0
>>> 1 and 0
0
>>> 1 and 1
1
>>> 
>>> # o and 1 represents output of 2 conditons
>>> x = 20
>>> y = 10
>>> x
20
>>> y
10
>>> x == 20
True
>>> y > 20
False
>>> x == 20 and y > 20
False
>>> # when we want to test 2 conditions then we use logical and
>>> x == 20 and y ==10
True
>>> # or
>>> x
20
>>> y
>>> y
10
>>> x == 50 or y == 100
False
>>> False or False
False
>>> True or False
True
>>> False or True
True
>>> True or True
True
>>> # not : negation
>>> # True , make it False and voceversa
>>> not
SyntaxError: invalid syntax
>>> not True
False
>>> not False
True
>>> not x >99
True
>>> x>99
False
>>> not y==10
False
>>> y==10
True
>>> ###########################
>>> # In programming, True means 1 and False means 0
>>> True + True
2
>>> False - True
-1
>>> (x == 20 and y == 10) and (x != 5 and y!= 20)
True
>>> z = 90
>>> x == 20 and z != -1 and y ==10
True
>>> not(x == 20 and z != -1 and y ==10)
False
>>> ###########################
>>> # Type casting
>>> # Type conversion: converting a data from one type to other
>>> x = '12'
>>> # check data type
>>> type(x)
<class 'str'>
>>> # 2 types of conversion
>>> # Implict and explicit conversion
>>> # Implcite means conversion performed by python itself
>>> # Example
>>> 12/2
6.0
>>> 1 + 2.5
3.5
>>> 1 + 2.0
3.0
>>> # in case of numeric data types we have precision
>>> # priority: int,float,complex
>>> 2 + (3+2j)
(5+2j)
>>> # Excplicit conversion
>>> # perfoermed by user
>>> 2 + (3+2j)
(5+2j)
>>> int(2 + (3+2j))
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    int(2 + (3+2j))
TypeError: can't convert complex to int
>>> int(2 + 3.5)
5
>>> x
'12'
>>> int(x)
12
>>> float(x)
12.0
>>> complex(x)
(12+0j)
>>> bool(x)
True
>>> #except 0 False '' None all are True
>>> bool(-1)
True
>>> bool(0)
False
>>> bool('')
False
>>> bool(None)
False
>>> bool("")
False
>>> tuple(x)
('1', '2')
>>> x
'12'
>>> list(x)
['1', '2']
>>> x
'12'
>>> 24/3
8.0
>>> str(24/3)
'8.0'
>>> ###################
>>> str(3+4j)
'(3+4j)'
>>> float(3+4j)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    float(3+4j)
TypeError: can't convert complex to float
>>> int(3+4j)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    int(3+4j)
TypeError: can't convert complex to int
>>> 
= RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/input.py =
Enter your name:'Python'
Enter your age:34
'Python' 34
<class 'str'> <class 'str'>
>>> 
= RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/input.py =
Enter your name:'A'
Enter your age:33
'A' 33
<class 'str'> <class 'int'>
>>> 
= RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/17/input.py =
Enter your name:A
Enter your age:22
Enter your salary45000
A 22 45000.0
<class 'str'> <class 'int'> <class 'float'>
>>> 
