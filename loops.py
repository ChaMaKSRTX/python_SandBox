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
# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# while secret_number:    #you can use "True" here if you want
#     picked_number = int(input("Enter an integer Number:"))
    
#     if picked_number == secret_number:
#         print("""
#     +=====================================+
#     | Well done, muggle! You are free now.|
#     +=====================================+
#     """)
#         break
#     else:
#        print("""
#         +=================================+
#         | Ha ha! You're stuck in my loop! |
#         +=================================+
#         """)





##For loop
"""
        Another kind of loop available in Python comes from the observation that sometimes it's more important
         to count the "turns" of the loop than to check the conditions.
         For example:
                i = 0
                while i < 100:
                    # do_something()
                    i += 1
                    print(i)

        Actually, the for loop is designed to do more complicated tasks
                     – it can "browse" large collections of data item by item.
                     For example:
                            for i in range(100):
                                # do_something()
                                pass
                                print(i)

        There are some new elements. Let us tell you about them:

                    - the (for) keyword opens the for loop; 
                            note: 
                                – there's no condition after it;
                                         you don't have to think about conditions,
                                                 as they're checked internally, without any intervention;
                    - any variable after the for keyword is the control variable of the loop;
                             it counts the loop's turns, and does it automatically;
                    - the in keyword introduces a syntax element describing the range of possible values
                                                                     being assigned to the control variable;
                    - the range() function (this is a very special function) is responsible for generating all the desired values
                     of the control variable;
                            in our example, the function will create 
                                (we can even say that it will feed the loop with) subsequent values from the following set: 0, 1, 2 .. 97, 98, 99; 
                      note:
                             in this case, the range() function starts its job from 0 and finishes it one step (one integer number) before the value of its argument;
                    note the pass keyword inside the loop body
                             – it does nothing at all; it's an empty instruction 
                             – we put it here because the for loop's syntax demands at least one instruction 
                                    inside the body (by the way – if, elif, else and while express the same thing)


"""
# for i in range(10):
#     print("The value of i is currently", i)

# Note:
# the loop has been executed ten times (it's the range() function's argument)
# the last control variable's value is 9 (not 10, as it starts from 0, not from 1)


#The range() function invocation may be equipped with two arguments, not just one:
# for i in range(2, 8):
#     print("The value of i is currently", i)

"""
    In this case, the first argument determines the initial (first) value of the control variable.


        The last argument shows the first value the control variable will not be assigned.

        Note: the range() function accepts only integers as its arguments, and generates sequences of integers.

        Can you guess the output of the program? Run it to check if you were right now, too.

        The first value shown is 2 (taken from the range()'s first argument.)

        The last is 7 (although the range()'s second argument is 8).

"""

#More about the for loop and the range() function with three arguments
#The range() function may also accept three arguments
# for i in range(2, 8, 3):
#     print("The value of i is currently", i)

"""
    The third argument is an increment – it's a value added to control the variable at every loop turn
             (as you may suspect, the default value of the increment is 1).

             output:
             The value of i is currently 2
             The value of i is currently 5


             The first argument passed to the range() function tells us what the starting number of the sequence is 
                        (hence 2 in the output). The second argument tells the function where to stop the sequence 
                                (the function generates numbers up to the number indicated by the second argument, 
                                        but does not include it). Finally, the third argument indicates the step, 
                                                which actually means the difference between each number
                                                         in the sequence of numbers generated by the function.

             2 (starting number) → 5 (2 increment by 3 equals 5 
                    – the number is within the range from 2 to 8) → 8
                        (5 increment by 3 equals 8 – the number is not within the range from 2 to 8,
                             because the stop parameter is not included in the sequence of numbers generated by the function.)
"""
#Note: if the set generated by the range() function is empty, the loop won't execute its body at all.
#For example
# for i in range(1, 1):
#     print("The value of i is currently", i)


"""
        Note: the set generated by the range() has to be sorted in ascending order. 
                There's no way to force the range() to create a set in a different form when the range() function 
                        accepts exactly two arguments. This means that the range()'s second argument must be greater than the first.

"""
#For example
# for i in range(2, 1):
#     print("The value of i is currently", i)


#short program to write some of the first powers of two:
# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2



#LAB
"""
        Scenario:
            Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States.
                     The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States 
                            (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!

            The word Mississippi is also used for a slightly different purpose: to count mississippily.

            If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.

            The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.

            Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"

            Use the skeleton we've provided in the editor.

            EXTRA INFO  
            Note that the code in the editor contains two elements which may not be fully clear to you at this moment: the import time statement, and the sleep() method. We're going to talk about them soon.

            For the time being, we'd just like you to know that we've imported the time module and used the sleep() method to suspend the execution of each subsequent print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. Don't worry - you'll soon learn more about modules and methods.
"""
#Code Solution
import time

# Write a for loop that counts to five.
for miss in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(miss, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)

# Write a print function with the final message.
print("Ready or not, here I come!")



#The break and continue statements

"""
    we've treated the body of the loop as an indivisible and inseparable sequence of instructions that are performed completely
             at every turn of the loop. However, as a developer, you could be faced with the following choices:

        - it appears that it's unnecessary to continue the loop as a whole;
                 you should refrain from further execution of the loop's body and go further;
        - it appears that you need to start the next turn of the loop without completing the execution of the current turn.
                Python provides two special instructions for the implementation of both these tasks.
                 Let's say for the sake of accuracy that their existence in the language is not necessary 
                    – an experienced programmer is able to code any algorithm without these instructions.
                         Such additions, which don't improve the language's expressive power,
                                 but only simplify the developer's work, are sometimes called
                                                             syntactic candy, or syntactic sugar.

        These two instructions are:

        01. break:
                 – exits the loop immediately, and unconditionally ends the loop's operation;
                         the program begins to execute the nearest instruction after the loop's body;
        02. continue:
                 – behaves as if the program has suddenly reached the end of the body;
                         the next turn is started and the condition expression is tested immediately.
        ** - Both these words are keywords.
"""
#For example
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break   #when it reacheas number three it breaks the execution
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue    # when it reaches number three it jumps and continue to the next number within the loop
    print("Inside the loop.", i)
print("Outside the loop.")



#LAB    The break statement – Stuck in a loop
"""
        Scenario:
            The break statement is used to exit/terminate a loop.

            Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

            Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
"""
#Code solution a win is a win
word = "chupacabra"

while True:
    user_word = input("Enter the word:")
    if user_word == word:
        print("You've successfully left the loop.")
        break
    else:
        user_word = input("Enter the word:")


#LAB   The continue statement – the Ugly Vowel Eater
"""
        Scenario:
            The continue statement is used to skip the current block and move ahead to the next iteration, 
            without executing the statements inside the loop.

            It can be used with both the while and for loops.

            Your task here is very special: you must design a vowel eater! Write a program that uses:

            a for loop;
            the concept of conditional execution (if-elif-else)
            the continue statement.

            Your program must:

            - ask the user to enter a word;
            - use user_word = user_word.upper() to convert the word entered by the user to upper case; 
                    we'll talk about string methods and the upper() method very soon – don't worry;
            - use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U 
                    from the inputted word;
            - print the uneaten letters to the screen, each one of them on a separate line.
                    Test your program with the data we've provided for you.

                    Solution:
                    # Prompt the user to enter a word
                    # and assign it to the user_word variable.
                    user_word = input("Enter the Word:")

                    user_word = user_word.upper()

                    for letter in user_word:
                        # Complete the body of the for loop.
                        if letter in "AEIOU":
                            continue
                        print(letter)




"""
#Code solution
# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to uppercase
user_word = user_word.upper()

# Iterate through each letter in the word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in 'AEIOU':
        continue  # Skip the rest of the loop and move to the next letter
    # Print the consonant (non-vowel) letters
    print(letter)


#LAB
"""
        Scenario:
            Your task here is even more special than before: you must redesign the (ugly) vowel eater
                     from the previous lab and create a better, upgraded (pretty) vowel eater! Write a program that uses:

            a for loop;
            the concept of conditional execution (if-elif-else)
            the continue statement.
            Your program must:

            ask the user to enter a word;
            - use user_word = user_word.upper() to convert the word entered by the user to upper case;
                     we'll talk about string methods and the upper() method very soon - don't worry;
            - use conditional execution and the continue statement to "eat" the following vowels 
                    A, E, I, O, U from the inputted word;
            - assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
            
"""

#Code Solution
# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to uppercase
user_word = user_word.upper()

# Initialize an empty string to store the word without vowels
word_without_vowels = ""

# Iterate through each letter in the word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in 'AEIOU':
        continue  # Skip the rest of the loop and move to the next letter
    # Concatenate consonants to the word_without_vowels variable
    word_without_vowels += letter

# Print the word without vowels
print("Word without vowels:", word_without_vowels)


#The while loop and the else branch
"""
        As you may have suspected, loops may have the else branch too, like ifs.

        The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.
"""
#code
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#Modify the snippet a bit so that the loop has no chance to execute its body even once:
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#The while's condition is False at the beginning




#The for loop and the else branch
#for loops behave a bit differently when combined with else

for i in range(5):
    print(i) #prints 0 1 2 3 4
else:
    print("else:", i)   #prints 4


#another example
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)   #outputs 111 and the loop body is not printed
"""
        The loop's body won't be executed here at all. Note: we've assigned the i variable before the loop.

        Run the program and check its output.

        When the loop's body isn't executed, the control variable retains the value it had before the loop.

        Note: if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the else branch.
"""

#LAB Essentials of the while loop

"""
        Scenario:
            Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

            Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.


            The figure illustrates the rule used by the builders:



            Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

            Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

            Test your code using the data we've provided.
"""
#Code Solution
# Ask the user to enter the total number of blocks
blocks = int(input("Enter the number of blocks: "))

# Initialize variables for height and blocks used
height = 0
blocks_used = 0
needed_blocks = 1  # Blocks needed for the first layer

# While we have enough blocks to complete the next layer
while blocks_used + needed_blocks <= blocks:
    # Increase the height of the pyramid
    height += 1
    
    # Add the blocks for this layer to the total used blocks
    blocks_used += needed_blocks
    
    # Increase the needed blocks for the next layer
    needed_blocks += 1

# Output the height of the pyramid
print("The height of the pyramid:", height)

"""
        Explanation of the Code
User Input:

blocks = int(input("Enter the number of blocks: ")) asks the user to enter the total number of blocks available.
Initialization:

height = 0 starts the height of the pyramid at zero.
blocks_used = 0 keeps track of the total blocks used so far.
needed_blocks = 1 represents the number of blocks needed for the first layer (1 block).
Loop to Build Layers:

while blocks_used + needed_blocks <= blocks: checks if we have enough blocks to complete the current layer. If yes:
height += 1 increments the height by 1, indicating a fully completed layer.
blocks_used += needed_blocks updates the count of blocks used.
needed_blocks += 1 increases the number of blocks needed for the next layer by 1.
Output the Result:

After the loop completes, print("The height of the pyramid:", height) outputs the maximum height of the pyramid that can be built with the given blocks.
Example Walkthrough
Example 1:
Input: blocks = 6
Process:
Layer 1 needs 1 block (height = 1, blocks used = 1)
Layer 2 needs 2 blocks (height = 2, blocks used = 3)
Layer 3 needs 3 blocks, but only 3 blocks remain, so the loop stops.
Output: The height of the pyramid: 2
Example 2:
Input: blocks = 15
Process:
Layer 1 needs 1 block (height = 1, blocks used = 1)
Layer 2 needs 2 blocks (height = 2, blocks used = 3)
Layer 3 needs 3 blocks (height = 3, blocks used = 6)
Layer 4 needs 4 blocks (height = 4, blocks used = 10)
Layer 5 needs 5 blocks, but only 5 blocks remain, so the loop stops.
Output: The height of the pyramid: 4
This code efficiently calculates the pyramid height by adding layers until we no longer have enough blocks for the next layer.
"""


#LAB   Collatz's hypothesis
"""
        Scenario:
            In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

            take any non-negative and non-zero integer number and name it c0;
            if it's even, evaluate a new c0 as c0 ÷ 2;
            otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
            if c0 ≠ 1, go back to point 2.
            The hypothesis says that regardless of the initial value of c0, it will always go to 1.

            Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.

            Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

            Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.
"""
#Code Solution
# Ask the user to enter a natural number
c0 = int(input("Enter a natural number: "))

# Initialize step counter
steps = 0

# Loop until c0 becomes 1
while c0 != 1:
    print(c0)  # Print the current value of c0
    
    # Apply Collatz rules
    if c0 % 2 == 0:
        c0 //= 2  # If c0 is even, divide it by 2
    else:
        c0 = 3 * c0 + 1  # If c0 is odd, calculate 3 * c0 + 1
    
    # Increase step count
    steps += 1

# Print the last value (which is 1)
print(c0)
# Output the total number of steps taken
print("Steps =", steps)

"""
        Explanation of the Code
User Input:

c0 = int(input("Enter a natural number: ")) prompts the user to enter a positive integer (c0). The integer is stored as the starting value of c0.
Initialization of Step Counter:

steps = 0 initializes a counter to track how many steps it takes to reduce c0 to 1.
Loop to Apply Collatz Rules:

The while c0 != 1 loop continues as long as c0 is not equal to 1.
Inside the loop:
print(c0) outputs the current value of c0.
If c0 is even (c0 % 2 == 0), c0 //= 2 divides it by 2.
If c0 is odd, c0 = 3 * c0 + 1 multiplies it by 3 and adds 1.
After each transformation, steps += 1 increments the step counter by 1.
Output the Final Step Count:

When c0 reaches 1, the loop stops.
The final value of c0 (1) is printed, followed by the total number of steps.
"""

#Section summary
"""
        1. There are two types of loops in Python: while and for:

the while loop executes a statement or a set of statements as long as a specified boolean condition is true, e.g.:

# Example 1
while True:
    print("Stuck in an infinite loop.")
 
# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
 
the for loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set – you will learn about them soon) or other iterable objects (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function. Look at the examples below:

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")
 
# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
 
2. You can use the break and continue statements to change the flow of a loop:

You use break to exit a loop, e.g.:

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
 
You use continue to skip the current iteration, and continue with the next iteration, e.g.:

text = "pyxpyxpyx
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
 
3. The while and for loops can also have an else clause in Python. The else clause executes after the loop finishes its execution as long as it has not been terminated by break, e.g.:


n = 0
 
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
 
print()
 
for i in range(0, 3):
    print(i)
else:
    print(i, "else")
 
4. The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:


start is an optional parameter specifying the starting number of the sequence (0 by default)
stop is an optional parameter specifying the end of the sequence generated (it is not included),
and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
Example code:


for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2
 
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
 
"""