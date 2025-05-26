"""
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text/ string Data Type:	str
Numeric Data Types:	int, 
                    float, 
                    complex.
Sequence Data Types:	list, 
                        tuple, 
                        range.
Mapping Data Type:	dict
Set Data Types:	set, 
                frozenset.
Boolean Data Type:	bool
Binary Data Types:	bytes,
                     bytearray, 
                     memoryview.
None Data Type:	NoneType

"""

##  Text/ string(str) Data Type:
name = "Chamak"
second_name = 'T*X'
word = """ How can you fly to the moon"""
l_word = '''Space ship'''
#print(f"{name} {second_name},{word} i'll use {l_word}")





##  Numeric Data Types:

### int
a = 2 




### float
#b = 4.6 



### complex
c = 4j



#print(a)
#print(b)
#print(c)
#print(f"the type of variable having, {a} is, {type(a)}")
#print(f"the type of variable having, {b} is, {type(b)}")
#print(f"the type of variable having, {c} is, {type(c)}")





##  Sequence Data Types:

### Lists
numbers = [10, 5, 7, 2, 1]
#print(f"{numbers}, {type(numbers)}")



### Tuples
fruits = ("apple", "banana", "cherry")
#print(f"{fruits}, {type(fruits)}")



### Range
number = range(10)
#print(f"{number}, {type(number)}")




##  Mapping Data Type:	

###  dict
person = {"name" : "John", "age" : 36}
#print(f"{person}, {type(person)}")





##  Set Data Types:

### set
fruits = {"apple", "banana", "cherry"}
#print(f"{fruits}, {type(fruits)}")



### frozenset
fruits = frozenset({"apple", "banana", "cherry"})
#print(f"{fruits}, {type(fruits)}")





##  Boolean Data Type:

### True and False
#print(10 > 5)
#print(5 > 10)
#first_number = int(input("Enter the first Number:"))
#second_number = int(input("Enter the Second Number:"))

#if first_number > second_number:
#    print(f"{first_number} is greater than {second_number}")
#else:
#    print(f"{second_number} is greater than {first_number}")





##  Binary Data Types:

### bytes
x = b"Hello"
#print(f"{x}, {type(x)}")



### bytearray
x = bytearray(5)
#print(f"{x}, {type(x)}")




### memoryview
x = memoryview(bytes(5))
#print(f"{x}, {type(x)}")





##  None Data Type:
### NoneType
x = None
print(f"{x}, {type(x)}")