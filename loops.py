#loops in Python
#while loop and for loop

"""
        while loop:
              repeats the execution as long as the condition evaluates to True.

              In general, in Python, a loop can be represented as follows:

                while
                    instruction


            for more than one instruction,
                while conditional_expression:
                    instruction_one
                    instruction_two
                    instruction_three
                    :
                    :
                    instruction_n


            It is now important to remember that:

            - if you want to execute more than one statement inside one while loop, 
                        you must (as with if) indent all the instructions in the same way;
            - an instruction or set of instructions executed inside the while loop is called the loop's body;
            - if the condition is False (equal to zero) as early as when it is tested for the first time,
                         the body is not executed even once (note the analogy of not having to do anything 
                                    if there is nothing to do);
            - the body should be able to change the condition's value,
                         because if the condition is True at the beginning, the body might run continuously to infinity.
                                     – notice that doing a thing usually decreases the number of things to do).


        An infinite loop:(endless loop)
                     is a sequence of instructions in a program which repeat indefinitely (loop endlessly.)
                For example:
                    while True:
                        print("I'm stuck inside a loop.")


"""
# while True:
#     print("I'm stuck inside a loop.")
# #press  ctrl + c to stop/ Keyboardinterrupt

#LAB
# Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)

#LAB 01
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))

# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)


#Using a counter variable to exit a loop
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

#more compact than the first one
# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

#LAB
"""
    Scenario:
        A junior magician has picked a secret number. He has hidden it in a variable named secret_number. 
                He wants everyone who runs his program to play the Guess the secret number game, and guess what number he has picked for them.
                  Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

        Your task is to help the magician complete the code in the editor in such a way so that the code:

        will ask the user to enter an integer number;
        will use a while loop;
        will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
        The magician is counting on you! Don't disappoint him.

        EXTRA INFO  
        By the way, look at the print() function. The way we've used it here is called multi-line printing. You can use triple quotes to print strings on multiple lines in order to make text easier to read, or create a special text-based design. Experiment with it.
"""
#code
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while secret_number:    #you can use "True" here if you want
    picked_number = int(input("Enter an integer Number:"))
    
    if picked_number == secret_number:
        print("""
    +=====================================+
    | Well done, muggle! You are free now.|
    +=====================================+
    """)
        break
    else:
       print("""
        +=================================+
        | Ha ha! You're stuck in my loop! |
        +=================================+
        """)





