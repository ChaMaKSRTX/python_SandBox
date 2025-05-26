#COMMENTS
"""
        A comment:
            is aremark inserted into a program which is omitted at a runtime.
        - it begins with a hash(#) sign

         Although it must be stated that the best way of commenting variables 
         is to name them in an unambiguous manner.
         For example area_of_squre
                        has a bit of meaning than using area_joe to initiate a variable
                            That is good for self commmenting.
"""





#Single comment are written as this 
# -- this is a single comment

#Multiline comment
#this is 
#a multline
#comment

#Since python ignorea strings which are not assigned to variable you can use triple quotes to assign multiline comment
"""
if 5 > 2:
print("its true") #This is the wrong way to do it
"""

""" is good to write code with a proper indentation as wrong indentation can result into an error"""
if 5 > 2:
    print("its true")#this is the right way to do it







# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
#a = 3.0
#b = 4.0
#c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of a square root.
#print("c =", c)

# This is a test program.
x = 1
y = 2
#y = y + x # uncomment this one to see the difference
#print(x + y)

"""
        01. Comments can be used to leave additional information in code.
                 They are omitted at runtime.
                     The information left in the source code is addressed to human readers.
                       In Python, a comment is a piece of text that begins with #.
                         The comment extends to the end of the line.

        02. If you want to place a comment that spans several lines,
                         you need to place # in front of them all. 
                                    Moreover, you can use a comment to mark a piece of code that is not needed at the moment.
                                      for example:

                                        # This program prints
                                        # an introduction to the screen.
                                        print("Hello!")  # Invoking the print() function
                                        # print("I'm Python.")
                                        
        03. self-commenting names to variables is the best practice.
                            for example:
                                  if you're using two variables to store the length and width of something, 
                                  the variable names length and width may be a better choice
                                                                         than myvar1 and myvar2.

        04. It's important to use comments to make programs easier to understand,
                 and to use readable and meaningful variable names in code.
                     However, it's equally important not to use variable names that are confusing,
                             or leave comments that contain wrong or incorrect information!

        05. Comments can be important when you are reading your own code after some time.
                (trust us, developers do forget what their own code does),
                    and when others are reading your code (they can help them understand 
                                                        what your programs do and how they do it more quickly).
"""
