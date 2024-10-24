"""
        Conditions and conditional execution:
        Conditions enables to have a  mechanism which will allow you to do something if a condition is met, 
            and not do it if it isn't.
        
        To make such decisions, Python offers a special instruction. Due to its nature and its application,
             it's called a conditional instruction (or conditional statement).
                For example:
                        if true_or_not:
                            do_this_if_true

        01. Conditional execution (if.. statement)
            This conditional statement consists of the following, strictly necessary,
                 elements in this and this order only:

                        01. the if keyword;
                        02. one or more white spaces;
                        03. an expression (a question or an answer) whose value will be
                                             interpreted solely in terms of True (when its value is non-zero)
                                                                         and False (when it is equal to zero);
                        04. a colon followed by a newline;
                        05. an indented instruction or set of instructions (at least one instruction is absolutely required);
                                     the indentation may be achieved in two ways
                                         by inserting a particular number of spaces 
                                         (the recommendation is to use four spaces of indentation),
                                           or by using the tab character; note: if there is more than one instruction in the indented part,
                                             the indentation should be the same in all lines; even though it may look the same if you use tabs mixed with spaces,
                                               it's important to make all indentations exactly the same – Python 3 does not allow the mixing of spaces and tabs for indentation.
                        
                        How does that statement work?

                        01. If the true_or_not expression represents the truth (i.e., its value is not equal to zero),
                                the indented statement(s) will be executed;
                        02. if the true_or_not expression does not represent the truth (i.e., its value is equal to zero),
                                the indented statement(s) will be omitted (ignored), and the next executed instruction
                                     will be the one after the original indentation level.
                                     For example:
                                        if sheep_counter >= 120: # Evaluate a test expression
                                            sleep_and_dream() # Execute if test expression is True

                        ***- conditionally executed statements have to be indented.
                        if sheep_counter >= 120:
                            make_a_bed()
                            take_a_shower()
                            sleep_and_dream()
                        feed_the_sheepdogs()

                        As you can see, making a bed, taking a shower and falling asleep and dreaming
                          are all executed conditionally – when sheep_counter reaches the desired limit.

                        Feeding the sheepdogs, however, is always done (i.e., the feed_the_sheepdogs() function
                             is not indented and does not belong to the if block, which means it is always executed.)


        02. Conditional execution: (if-else statement)
            For example:
                if true_or_false_condition:
                    perform_if_condition_true
                else:
                perform_if_condition_false


            -another example:
                if the_weather_is_good:
                    go_for_a_walk()
                else:
                    go_to_a_theater()
                have_lunch()



            -another example:
            if the_weather_is_good:
                go_for_a_walk()
            have_fun()
            else:
                go_to_a_theater()
                enjoy_the_movie()
            have_lunch()


            ##- Nested if-else statements
            For example:
            if the_weather_is_good:
                if nice_restaurant_is_found:
                    have_lunch()
                else:
                    eat_a_sandwich()
            else:
                if tickets_are_available:
                     go_to_the_theater()
                else:
                    go_shopping()


        Here are two important points:

        01. this use of the if statement is known as nesting;
          remember that every else refers to the if which lies at the same indentation level;
            you need to know this to determine how the ifs and elses pair up;
                consider how the indentation improves readability,
                     and makes the code easier to understand and trace.

    03. Conditional execution ( elif statement )
            elif is used to check more than just one condition,
                 and to stop when the first statement which is true is found.
                    For example:
                        if the_weather_is_good:
                            go_for_a_walk()
                        elif tickets_are_available:
                            go_to_the_theater()
                        elif table_is_available:
                            go_for_lunch()
                        else:
                            play_chess_at_home()

                The way to assemble subsequent if-elif-else statements is sometimes called a cascade.
                        Some additional attention has to be paid in this case:

                        - you mustn't use else without a preceding if;
                        - else is always the last branch of the cascade, regardless of whether you've used elif or not;
                        - else is an optional part of the cascade, and may be omitted;
                        - if there is an else branch in the cascade, only one of all the branches is executed;
                        - if there is no else branch, it's possible that none of the available branches is executed.


"""

#Analyzing codes Samples
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# Print the result
#print("The larger number is:", larger_number)



#another example of the same codes above
# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Choose the larger number
# if number1 > number2: larger_number = number1   #this part is the same as above as there is only one instruction on that section
# else: larger_number = number2                   #however this style maybe missleading sometimes but is good to know it

# Print the result
#print("The larger number is:", larger_number)



#another code to determine largest number between three numbers
# Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
# largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3

# Print the result
#print("The largest number is:", largest_number)


#Pseudocode and algorithm
# largest_number = -999999999
# number = int(input("Enter Number:"))
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
# # Go to line 02
# print("Largest Number:", largest_number)

#Good thing is that Python comes many build-in function which can be used such as (max) and (min) to find the largerst and smallest value
# Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.

# largest_number = max(number1, number2, number3)

# # Print the result.
# print("The largest number is:", largest_number)


# Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.

# smallest_number = min(number1, number2, number3)

# # Print the result.
# print("The Smallest number is:", smallest_number)

#LAB 01
# name = input("Enter flower name: ")

# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif name == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", name + "!")
	
#LAB 02
"""
Scenario
Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.

Look at the code in the editor – it only reads one input value and outputs a result, so you need to complete it with some smart calculations.

Test your code using the data we've provided.


                Test Data
                Sample input:

                10000
                Expected output:

                The tax is: 1244.0 thalers
                Output

                Sample input:

                100000
                Expected output:

                The tax is: 19470.0 thalers
                Output
				
                Sample input:

                1000
                Expected output:

                The tax is: 0.0 thalers
                Output
				
                Sample input:

                -100
                Expected output:

                The tax is: 0.0 thalers
                Output
"""
# income = float(input("Enter the annual income: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
# 	tax = (income - 85528) * 0.32 + 14839.02

# if tax < 0.0:
# 	tax = 0.0

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
 


#LAB 03
# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
#     #  Write the if-elif-elif-else block here.
	
    #final code
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
	


#LAB 04
##
x = 5
y = 10
z = 8
 
print(x > y)
print(y > z)
 
 ##
x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)
 

##
x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z)
print((y - 5) == x)
 
 ##
x = 10
 
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")


##
x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
 

##
x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
 
 
 