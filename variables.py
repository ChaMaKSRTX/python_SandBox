#import sys
#print(sys.version) # prints out detailed version of python instelled

#Are containers for storing data values.
"""
    Do not need to be declared by any particular type,
      since type can be changed even after setting it.
    01. They can't have spaces (e.g., test var is not allowed)
    02. They can only include letters, numbers, and underscores (e.g., test_var! is not allowed)
    03. They have to start with a letter or underscore (e.g., 1_var is not allowed)
                    _vart = 23
                    tyyt = 21
                    print(_vart)
                    print(tyyt)
Then, to create the variable, you need to use = to assign the value that you want it to have.

You can always take a look at the value assigned to the variable by using print() and putting the name of the variable in parentheses."""

#creating a variable
numb = 2    #int
name = "Saint"  #string
decimal = 3.5   #float
bool = True     #boolean can True or False depending on the condition

#print(numb)
#print(name)
#print(decimal)
#print(bool)

#assingment
test_var = 4 + 5
#print(test_var)

#manipulating a variable
New_var = 3
#print(New_var)

New_var = 700   #manipulation
#print(New_var)

#print(test_var)
#print(New_var)


New_var = New_var ** 2
#print(New_var)

#Using multiple variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

days_per_year = 365.25
#Calculating the number of seconds for 4 years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
#print(total_secs)

#print(total_secs)

#global variables 
"""
Any variable created outside a function can be accessed within any function and so they have global scope."""

x = 5   #global variable
y = 10  #global variable
def sum():
    sum = x + y
    return sum
#print(sum())

#another example
second_word = "Awesome" #global variable

"""
def message():
    print(f"Python is, {second_word}")
message()
"""

# local variable 
"""
a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
"""
def message():
    second_word = "Fantastic" #local variable
    print(f"Python is, {second_word}")
message()

print(f"Python is, {second_word}")
