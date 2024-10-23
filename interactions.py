#input() function.
"""
    input() function reads data entered by the user process the data and return the reasonable result.
    
    Note:
    01. The program prompts the user to input some data from the console (most likely using a keyboard,
      although it is also possible to input data using voice or image).
    02. Input() function invoked without arguments is the simplest way of using the function
            the function will switch the console to input mode;
              you'll see a blinking cursor, and you'll be able to input some keystrokes,
                finishing off by hitting the Enter key; 
                    all the inputted data will be sent to your program through the function's result.
    03. assign variable so as to hold the result, this is crucial
                 ‒ missing out this step will cause the entered data to be lost,
                            then we use the print() function to output the data we get,
                              with some additional remarks.

    04. The result of the input() function is a string.
            A string containing all the characters the user enters from the keyboard.
                                                 It is not an integer or a float.
                This means that you mustn't use it as an argument of any arithmetic operation atleast for now.
"""
print("Tell me anything...")
anything = input()  #reads input from the user
#print("Hmm...", anything, "... Really?")

#input() function with an argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

"""
        - The input() function is invoked with one argument, it's a string containing a message;
        - The message will be displayed on the console before the user is given an opportunity to enter anything
         - input() will then do its job.
                    This variant of the input() invocation simplifies the code and makes it clearer.
"""
#input() function prohibited operations 
# Testing a TypeError message.

anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

            ###Type casting(type conversion)
"""
        Can be used to solve the input() function prohibited operations by simply converting the data received form user(numerical) 
"""
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

#string operator (+) and (*)
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5)
# print("+" + 10 * "-" + "+")

#type casting using str()
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))


# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# c = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is " + str(c))

# LAB operators and expresions
x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)


#LAB
"""
        Scenario:
            Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

            For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

            Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.

            Test your code carefully. Hint: using the % operator may be the key to success.
"""
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')

#Summary
"""
        1. The print() function sends data to the console, while the input() function gets data from the console.

        2. The input() function comes with an optional parameter: the prompt string. It allows you to write a message before the user input, e.g.:
                name = input("Enter your name: ")
                print("Hello, " + name + ". Nice to meet you!")
 
        3. When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking (it prompts the user to take action when the console is switched to input mode) until the user has entered an input and/or pressed the Enter key.

       4. The result of the input() function is a string. You can add strings to each other using the concatenation (+) operator.
         for example:

            num_1 = input("Enter the first number: ") # Enter 12
            num_2 = input("Enter the second number: ") # Enter 21
            
            print(num_1 + num_2) # the program returns 1221
            
      5. You can also multiply ((*)  replication) 
            for example:
            my_input = input("Enter something: ") # Example input: hello
            print(my_input * 3) # Expected output: hellohellohello
            
"""