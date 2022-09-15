"""NOTES for STUDYING"""
"""Print number"""
print("=====variables=====")
from ssl import DefaultVerifyPaths
import time
start_time = time.time()
print ("hello world")
i = 1000
love = 1000
you = 1000
print ("I love you" ,i + love + you)
print(time.time() - start_time, "seconds")
#comment
"""this is also comment"""
#compile file to bytecode by typing python -m py_compile Main.py
# space by using underscore(_)

"""data_types"""
#integer = bilangan bulat (gaad koma)
print("=====Data Types=====")
data_integer = 5
#print type to know the numbers type
print ("data : ", data_integer)
print("- type : ", type(data_integer))

#float = bilangan berkomaC C++
data_float = 7.2
print ("data : ", data_float)
print ("- type : ", type(data_float))

#string = characters
data_string = "dave"
print ("data : " , type (data_string))
print ("- type : ", data_string)

#boolean = binary number 0/1 or true/false
data_boolean = True
print ("data : " , data_boolean)
print ("- type : ", type(data_boolean))

#special data

#complex numbers
data_complex = complex (1,9)
print ("data : " , data_complex)
print ("- type : ", type(data_complex))

#data C language

from ctypes import c_double

data_c_double = c_double(10.7)
print ("data : " , data_c_double)
print ("- type : ", type(data_c_double))

"""CONVERSING/CASTING DATA"""
#integer to other data
#note if boolean=o, then false, elif boolean =/ 0 , then true
print("=====Conversing Data=====")
print("=====INTEGER=====")

data_int = 10;
print ("data =",data_int,"type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool= bool(data_int) 
print ("data =",data_float,"type =",type(data_float))
print ("data =",data_str,"type =",type(data_str))
print ("data =",data_bool,"type =",type(data_bool))

print("=====FLOAT=====")

data_float = 8.5
print("data =",data_float,"type =",type(data_float))

data_int = int(data_float)#are always rounded down
data_str = str(data_float)
data_bool= bool(data_float)
print ("data =",data_int,"type =",type(data_int))
print ("data =",data_str,"type =",type(data_str))
print ("data =",data_bool,"type =",type(data_bool))

print("=====BOOLEAN=====")

data_bool = True; #0 or 1, true or false
print("data =",data_bool,"type =",type(data_bool))

data_int = int(data_bool)#are always rounded down
data_float = float(data_bool)
data_str= str(data_bool)
print ("data =",data_int,"type =",type(data_int))
print ("data =",data_float,"type =",type(data_float))
print ("data =",data_str,"type =",type(data_str))

print("=====STRING=====")

data_str = "10"#if it is a alphabet then it will eventually error
print("data =",data_str,"type =",type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print ("data =",data_int,"type =",type(data_int))
print ("data =",data_float,"type =",type(data_float))
print ("data =",data_bool,"type =",type(data_bool))

print("=====INPUT DATA=====")
#always string
data = input("Input Data:")

print("data =",data,"type =",type(data))

data = input("Input Data:")

print("data =",data,"type =",type(data))

data_int = int(input("Input Number :"))
print("data =",data_int,"type =",type(data_int))

data_float = float(input("Input Decimal Number :"))
print("data =",data_float,"type =",type(data_float))

data_str = str(input("Input Alphabet ="))
print("data =",data_str, "type =", type(data_str))

data_bool = bool(int(input("Input Binary Number=")))
print("data =",data_bool, "type =",type(data_bool)) 

print("=====Arithmetic Operation")

x = 8
y = 2

#Addition
result = x + y
print(x,'+',y,'=',result)

#Substraction
result = x - y
print(x,'-',y,'=',result)

#Multiplication
result = x * y
print(x,'*',y,'=',result)

#Division
result = x / y
print(x,'/',y,'=',result)

#exponent
result = x ** y
print(x,'**',y,'=',result)

#modulus/modulo
result = x % y
print(x,'%',y,'=',result)

#floor division
result = x // y
print(x,'//',y,'=',result)

