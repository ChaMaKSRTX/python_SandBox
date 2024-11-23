"""
                Function:
                    is a reusable block of code that executes a certain functionality when its called.

                    Decomposition:
                        Breaking a large broblem into small part which are then used to make some function,
                                 which can later be brought together to solve the problem.




                    SECTION SUMMARY

                    1. A function is a block of code that performs a specific task when the function is called (invoked). You can use functions to make your code reusable, better organized, and more readable. Functions can have parameters and return values.

                    2. There are at least four basic types of functions in Python:

                            - built-in functions which are an integral part of Python (such as the print() function). 
                            - pre-installed modules (you'll learn about them in the Python Essentials 2 course)
                            - user-defined functions which are written by users for users ‒ you can write your own functions and use them freely in your code,
                            - the lambda functions (you'll learn about them in the Python Essentials 2 course.)
                    3. You can define your own function using the def keyword and the following syntax:

                    def your_function(optional parameters):
                        # the body of the function
                    
                    You can define a function which doesn't take any arguments, e.g.:


                    def message(): # defining a function
                        print("Hello") # body of the function
                    
                    message() # calling the function
                    
                    You can define a function which takes arguments, too, just like the one-parameter function below:


                    def hello(name): # defining a function
                        print("Hello,", name) # body of the function
                    
                    
                    name = input("Enter your name: ")
                    
                    hello(name) # calling the function

"""

def hello(name): # defining a function
    print("Hello,", name) # body of the function
                    
                    
name = input("Enter your name: ")
                    
hello(name) # calling the function



#how functions communicate with their environment
#positional parameter
def name(first_name, second_name):
    print(f"My name is {first_name} {second_name}")

first_name = input("Enter your First Name:")

second_name = input("Enter your Second Name:")

name(first_name, second_name)


#mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)#positional argument 

adding(c = 1, a = 2, b = 3)#keyword argument

adding(3, c = 1, b = 2)#positional and keyword argument mixing in a function

adding(4, 3, c = 2)

#parametrized function more details
"""
  It happens at times that a particular parameter's values are in use more often than others. 
    Such arguments may have their default (predefined) values taken into consideration when their corresponding arguments have been omitted.


They say that the most popular English last name is Smith. Let's try to take this into account.
"""
#run the code below
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")

introduction("Henry")

introduction(first_name="William")



#this makes this code valid
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()

introduction(last_name="Hopkins")

"""
  SECTION SUMMARY
1. You can pass information to functions by using parameters.
   Your functions can have as many parameters as you need.

An example of a one-parameter function:


def hi(name):
    print("Hi,", name)
 
hi("Greg")


An example of a two-parameter function:

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)
 
hi_all("Sebastian", "Konrad")
 

An example of a three-parameter function:

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
 
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)
 
2. You can pass arguments to a function using the following techniques:

positional argument passing in which the order of arguments passed matters (Ex. 1)
keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2)
a mix of positional and keyword argument passing (Ex. 3.)

Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # outputs: 3
subtra(2, 5) # outputs: -3
 
 
Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # outputs: 3
subtra(b=2, a=5) # outputs: 3
 
Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(5, 2) # outputs: 3
 
It's important to remember that positional arguments mustn't follow keyword arguments.
   That's why if you try to run the following snippet:


def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(a=5, 2) # Syntax Error
 
Python will not let you do it by signalling a SyntaxError.

3. You can use the keyword argument-passing technique to pre-define a value for a given argument:


def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # outputs: Andy Smith
name("Betty", "Johnson") # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
 
"""
#code
def intro(a="James Bond", b="Bond"):
     print("My name is", b + ".", a + ".")

intro()

#code
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")

#code
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")


def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
#SyntaxError - a non-default argument (c) follows a default argument (b=2).


#Returning a result from function
#Effect and results
#return instruction
#return without an expression
def happy_new_year(wishes = True):#with a True function
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return #no expression

    print("Happy New Year!")

happy_new_year()


def happy_new_year(wishes = False): #with a False function
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")

happy_new_year()


#return with an expression
#def function():
#    return expression

#code
def boring_function():
    return 123

x = boring_function

print("The boring function as retur it's result. It's:", x)

#it's allowed to ignore a function
#the function below ignores the return value
def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")


#A few words about None
#Its data doesn't represent any reasonable value ‒ actually, 
# it's not a value at all; hence, it mustn't take part in any expressions.
print(None + 2)

#will cause a runtime error, described by the following diagnostic message:
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#Note: None is a keyword.
#There are only two kinds of circumstances when None can be safely used:

#when you assign it to a variable (or return it as a function's result)
#when you compare it with a variable to diagnose its internal state.
value = None
if value is None:
    print("Sorry, you don't carry any value")

#Don't forget this: if a function doesn't return a certain value using a return expression clause,
#  it is assumed that it implicitly returns None.
#code
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2)) #True
print(strange_function(1)) #None


#list as a function argument
#code
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

#print(list_sum(5))

#code
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

#print(list_sum(5))

#list as a function result
#Any entity recognizable by Python can be a function result.
#code
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


#LAB
#write and test a function which takes one argument (a year)
#  and returns True if the year is a leap year, or False otherwise.
#code 01
#promit the user to insert data of the year
def is_leap_year(year):
    """
    Determine whether a given year is a leap year.
    
    Args:
        year (int): The year to check.
        
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # A year is a leap year if it is divisible by 4 and not divisible by 100,
    # or if it is divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Testing the function
test_year = int(input("Enter a year: "))
if is_leap_year(test_year):
    print(f"{test_year} is a leap year.")
else:
    print(f"{test_year} is not a leap year.")


#code 02 with given data
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


#LAB How many days: writing and using a functions
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


#code 02
#calculates number of days in a month of the year
def days_in_month(year, month):
    """
    Returns the number of days in a given year and month.

    Args:
        year (int): The year to check (must be a valid positive integer).
        month (int): The month to check (must be an integer between 1 and 12).

    Returns:
        int or None: The number of days in the month for the given year, 
                     or None if the inputs are invalid.
    """
    # Check if year is valid (must be a positive integer)
    if year < 1 or not isinstance(year, int):
        return None

    # Check if month is valid (must be between 1 and 12)
    if month < 1 or month > 12 or not isinstance(month, int):
        return None

    # Define the number of days in each month for a non-leap year
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the month is February and if the year is a leap year
    if month == 2 and is_leap_year(year):
        return 29  # February in a leap year has 29 days

    # Return the days for the month
    return days_in_months[month - 1]


def is_leap_year(year):
    """
    Determines if a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Test the function
test_year = int(input("Enter a year: "))
test_month = int(input("Enter a month: "))
days = days_in_month(test_year, test_month)

if days is None:
    print("Invalid year or month!")
else:
    print(f"The number of days in {test_year}-{test_month} is {days}.")








# LAB Day of the year:
"""
  Your task is to write and test a function which takes three arguments
     (a year, a month, and a day of the month) and returns the corresponding day of the year,
        or returns None if any of the arguments is invalid.
"""
#code 01
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))


#code 02
def day_of_year(year, month, day):
    """
    Returns the day of the year for a given date.
    
    Args:
        year (int): The year of the date.
        month (int): The month of the date (1-12).
        day (int): The day of the month.
        
    Returns:
        int or None: The day of the year if valid; None otherwise.
    """
    # Check if year is valid
    if year < 1 or not isinstance(year, int):
        return None
    
    # Check if month is valid
    if month < 1 or month > 12 or not isinstance(month, int):
        return None

    # Define the number of days in each month for a non-leap year
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February for leap years
    if is_leap_year(year):
        days_in_months[1] = 29

    # Check if the day is valid for the given month
    if day < 1 or day > days_in_months[month - 1]:
        return None

    # Calculate the day of the year
    return sum(days_in_months[:month - 1]) + day


def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    
    Args:
        year (int): The year to check.
        
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Test the function
test_year = int(input("Enter a year: "))
test_month = int(input("Enter a month: "))
test_day = int(input("Enter a day: "))
day_number = day_of_year(test_year, test_month, test_day)

if day_number is None:
    print("Invalid date!")
else:
    print(f"The day of the year for {test_year}-{test_month}-{test_day} is {day_number}.")







#LAB Prime numbers :
"""
  Your task is to write a function checking whether a number is prime or not.

The function:

is called is_prime;
takes one argument (the value to check)
returns True if the argument is a prime number, and False otherwise.
Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder 
‒ if it's zero, your number cannot be a prime; think carefully about when you should stop the process.

If you need to know the square root of any value, you can utilize the ** operator. 
Remember: the square root of x is the same as x0.5
"""
#A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
#code 01
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


#code02
def is_prime(number):
    """
    Checks whether a number is a prime number.

    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if the number is a prime number, False otherwise.
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check divisors from 2 to the square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False  # Not a prime number if divisible

    return True  # The number is prime


# Testing the function
test_number = int(input("Enter a number to check if it is prime: "))
if is_prime(test_number):
    print(f"{test_number} is a prime number.")
else:
    print(f"{test_number} is not a prime number.")








#LAB   Converting fuel consumption:

"""
 A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

The functions:

are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
take one argument (the value corresponding to their names)
Complete the code in the editor and run it to check whether your output is the same as ours.

Here is some information to help you:

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
"""
#code 01
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


#code 02
def liters_100km_to_miles_gallon(liters_per_100km):
    """
    Converts fuel consumption from liters per 100 kilometers to miles per gallon.

    Args:
        liters_per_100km (float): Fuel consumption in liters per 100 kilometers.

    Returns:
        float: Fuel consumption in miles per gallon.
    """
    # Conversion factors
    miles_per_kilometer = 1609.344 / 1000  # 1 mile = 1609.344 meters
    kilometers_per_100km = 100  # There are 100 kilometers in the given value
    liters_per_gallon = 3.785411784  # 1 gallon = 3.785411784 liters

    # Convert
    miles_per_100km = kilometers_per_100km / miles_per_kilometer
    miles_per_gallon = miles_per_100km / liters_per_100km

    return miles_per_gallon


def miles_gallon_to_liters_100km(miles_per_gallon):
    """
    Converts fuel consumption from miles per gallon to liters per 100 kilometers.

    Args:
        miles_per_gallon (float): Fuel consumption in miles per gallon.

    Returns:
        float: Fuel consumption in liters per 100 kilometers.
    """
    # Conversion factors
    miles_per_kilometer = 1609.344 / 1000  # 1 mile = 1609.344 meters
    kilometers_per_100km = 100  # There are 100 kilometers in the given value
    liters_per_gallon = 3.785411784  # 1 gallon = 3.785411784 liters

    # Convert
    kilometers_per_gallon = miles_per_gallon * miles_per_kilometer
    liters_per_100km = liters_per_gallon / kilometers_per_gallon * kilometers_per_100km

    return liters_per_100km


# Test cases
print(liters_100km_to_miles_gallon(3.9))  # 60.31143158017339
print(liters_100km_to_miles_gallon(7.5))  # 31.36194444444444
print(liters_100km_to_miles_gallon(10.0))  # 23.52145833333333

print(miles_gallon_to_liters_100km(60.3))  # 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4))  # 7.490910297239916
print(miles_gallon_to_liters_100km(23.5))  # 10.006949125512594

#SECTION SUMMARY
"""
  1. You can use the return keyword to tell a function to return some value. The return statement exits the function, e.g.:


def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # outputs: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # outputs: None
 
2. The result of a function can be easily assigned to a variable, e.g.:


def wishes():
    return "Happy Birthday!"
 
w = wishes()
 
print(w) # outputs: Happy Birthday!
 
Look at the difference in output in the following two examples:


# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"
 
wishes() # outputs: My Wishes
 
 
# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"
 
print(wishes())
 
# outputs: My Wishes
# Happy Birthday
 
3. You can use a list as a function's argument, e.g.:


def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)
 
hi_everybody(["Adam", "John", "Lucy"])
 
4. A list can be a function result, too, e.g.:


def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(create_list(5))
 
"""
#code
def hi():
    return
    print("Hi!")

hi() #The function will return an implicit None value.



#code
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5)) #True
print(is_int(5.0)) #False
print(is_int("5")) #None



#code
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11)) #Output is [0, 2, 4, 6, 8, 10]

#code
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo)) #Output is [1, 4, 9, 16, 25]






