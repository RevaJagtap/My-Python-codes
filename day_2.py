Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # identifier
>>> # is an identity of an object
>>> 100
100
>>> 'py'
'py'
>>> 12.55
12.55
>>> id(100)
140735952969856
>>> a = 100 # a is an identifier , 100 is an object
>>> a
100
>>> s = 'py' # s is an identifier , py is an object
>>> s
'py'
>>> # Rules for giving identifiers
>>> # Characters, words and _ are allowed
>>> a
100
 
>>> bank = 'SBI'
>>> bank
'SBI'
>>> _b = 300
>>> _b
300
>>> # when we have 2 words
>>> bank ifsc = 'SBI12345'
SyntaxError: invalid syntax
>>> # space between 2 char/string is nnot allowed
>>> bank_ifsc = 'SBI12345'
>>> bank_ifsc
'SBI12345'
>>> # Special symbols and charcters are not allowed
>>> # !~@$%^&*()-:, etc
>>> @ = 'good morning'
SyntaxError: invalid syntax
>>> % = 33
SyntaxError: invalid syntax
>>> a$ = 33
SyntaxError: invalid syntax
>>> # Numbers as an identifiers not allowed
>>> 1 = 200
SyntaxError: can't assign to literal
>>> # but if we use num. as a suffix
>>> a4 = 33
>>> a4
33
>>> # its allowed
>>> a_4 = 33
>>> info_22 = 'akjhklj'
>>> info_22
'akjhklj'
>>> # But if we use num. as preffix : not allowed
>>> 4_b = 300
SyntaxError: invalid token
>>> 22_info = 'ewirywoieru'
SyntaxError: invalid token
>>> ##################################
>>> # Keywords:
>>> # Reserved keywords
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> # These keywords we can not use as an identifier
>>> del x = 111
SyntaxError: invalid syntax
>>> with = 444
SyntaxError: invalid syntax
>>> # lets check total no. of keywords
>>> len(keyword.kwlist)
35
>>> # if we want more info abt these keywords then use help() function
>>> help('in')
Membership test operations
**************************

The operators "in" and "not in" test for membership.  "x in s"
evaluates to "True" if *x* is a member of *s*, and "False" otherwise.
"x not in s" returns the negation of "x in s".  All built-in sequences
and set types support this as well as dictionary, for which "in" tests
whether the dictionary has a given key. For container types such as
list, tuple, set, frozenset, dict, or collections.deque, the
expression "x in y" is equivalent to "any(x is e or x == e for e in
y)".

For the string and bytes types, "x in y" is "True" if and only if *x*
is a substring of *y*.  An equivalent test is "y.find(x) != -1".
Empty strings are always considered to be a substring of any other
string, so """ in "abc"" will return "True".

For user-defined classes which define the "__contains__()" method, "x
in y" returns "True" if "y.__contains__(x)" returns a true value, and
"False" otherwise.

For user-defined classes which do not define "__contains__()" but do
define "__iter__()", "x in y" is "True" if some value "z" with "x ==
z" is produced while iterating over "y".  If an exception is raised
during the iteration, it is as if "in" raised that exception.

Lastly, the old-style iteration protocol is tried: if a class defines
"__getitem__()", "x in y" is "True" if and only if there is a non-
negative integer index *i* such that "x == y[i]", and all lower
integer indices do not raise "IndexError" exception.  (If any other
exception is raised, it is as if "in" raised that exception).

The operator "not in" is defined to have the inverse true value of
"in".

Related help topics: SEQUENCEMETHODS

>>> 'Sachin' in 'Sachin Tendulkar'
True
>>> 'Saurav' in 'Sachin Tendulkar'
False
>>> #################################
>>> # PEP8 standards
>>> x = 20
>>> x
20
>>> x=10
>>> x
10
>>> # identifiers should be in lowercase
>>> # if we want function_name then also lower case
>>> # if we want to give a class name : use cammel case
>>> # example: class Sample:
>>> # class SampleBank:
>>> ##################################
>>> # Operators in Python
>>> # Arithmatic
>>> # + - * / // % **
>>> 12 + 22
34
>>> 30 - 10
20
>>> 2 * 2
4
>>> 4/2
2.0
>>> # // floor division
>>> 10/3 #divide operator
3.3333333333333335
>>> 10//3 #floor-divide operator
3
>>> # 3(floor) . 33(ceil)
>>> 20/3
6.666666666666667
>>> 20//3
6
>>> round(22/3)
7
>>> # ** exponential operator
>>> # power of operator
>>> # square of 25
>>> 25**2
625
>>> # Cube of 3
>>> 3**3
27
>>> # Mod operator
>>> # return remainder
>>> 4%5
4
>>> 1%2
1
>>> 4%2
0
>>> # Assignment operator
>>> # +=, -=, *=.....
>>> # put = infront of arithmatic
>>> a
100
>>> a + 10
110
>>> # a is unchanged
>>> a
100
>>> a += 10 # a = a + 10
>>> a
110
>>> a += 200
>>> a
310
>>> a -= 210
>>> a
100
>>> a *= 2
>>> a
200
>>> a/= 10
>>> a
20.0
>>> a //= 2
>>> a
10.0
>>> a %= 5
>>> a
0.0
>>> #################################
>>> # Relational/ COnditional operators
>>> # these are used to compare 2 objects
>>> # < > <= >= == !=
>>> 2 < 1
False
>>> # When we use comparison operators, it always gives bool output [True, False]
>>> 2 > 1
True
>>> 2 <= 2
True
>>> 3 >= 1
True
>>> 'py' == 'py'
True
>>> 'py' == 'Py'
False
>>> 'py' != 'Py'
True
>>> ################################
>>> # Membership Operators
>>> # to check either the object is a part of collection or not
>>> # in
>>> # not in
>>> 10 in [10,20,30]
True
>>> 100 in [10,20,30]
False
>>> 'Amit' in 'Amitabh bachchan'
True
>>> 'bac' in 'Amitabh bachchan'
True
>>> 'b' in 'Amitabh bachchan'
True
>>> 'z' in 'Amitabh bachchan'
False
>>> 'z' not in 'Amitabh bachchan'
True
>>> 'a' in 'Sarang'
True
>>> 'e' in 'Sarang'
False
>>> 
