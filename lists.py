#LISTS
"""
    list:
             is a type of data in Python used to store multiple objects.
                    It is an ordered and mutable collection of comma-separated items between square brackets.

            or;
                Is a collection of elements, but each elemet is a scalar

            Note:
                01. Some of the key focus on list are index, update, and delete list elements.
                02. how to perform slices, 
                03. and how to use some of the most important list functions and methods.
                04. Scalars:
                         Simple variables which stores one type of data.

                Example:
                    numbers = [10, 5, 7, 2, 1]


                    uses:
                    - Used in scenarios which involves a large number of elements/value/data.


                    


            --- Indexing lists
                    making access or changes to the elements in a list.

                    Index:
                        a value inside the brackets which selects one elemets of the list.

                    Indexing:
                        Is the operation of selecting an element from the list.

                        For example:
                        numbers = [10, 5, 7, 2, 1]
                        print("Original list contents:", numbers)  # Printing original list contents.

                        numbers[0] = 111
                        print("New list contents: ", numbers)  # Current list contents.

                        Example 02:
                        numbers = [10, 5, 7, 2, 1]
                        print("Original list contents:", numbers)  # Printing original list contents.

                        numbers[0] = 111
                        print("\nPrevious list contents:", numbers)  # Printing previous list contents.

                        numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
                        print("New list contents:", numbers)  # Printing current list contents.

                Note:
                     any expression can be the index, too.


                     
                
                     

            --- Accessing list content
            Example:
                print(numbers[0]) # Accessing the list's first element.

            Example 02:
                numbers = [10, 5, 7, 2, 1]
                print("Original list contents:", numbers)  # Printing original list contents.

                numbers[0] = 111
                print("\nPrevious list contents:", numbers)  # Printing previous list contents.

                numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
                print("Previous list contents:", numbers)  # Printing previous list contents.

                print("\nList length:", len(numbers))  # Printing the list's length.
                print(numbers)  # Printing the whole list.


                




            --- The len() function:
                    Used to check the length of a list.

                    For example:
                        my_list = ["white", "purple", "blue", "yellow", "green"]
                        print(len(my_list))  # outputs 5

                        del my_list[2]
                        print(len(my_list))  # outputs 4





            ---  Removing elements from a list
                    Any of the list's elements may be removed at any time,
                       this is done with an instruction named del (delete).
                             Note: it's an instruction, not a function.

                             Example:
                                del numbers[1]
                                print(len(numbers))
                                print(numbers)

                            For example 01:
                            numbers = [10, 5, 7, 2, 1]
                            print("Original list content:", numbers)  # Printing original list content.

                            numbers[0] = 111
                            print("\nPrevious list content:", numbers)  # Printing previous list content.

                            numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
                            print("Previous list content:", numbers)  # Printing previous list content.

                            print("\nList's length:", len(numbers))  # Printing previous list length.

                            ###

                            del numbers[1]  # Removing the second element from the list.
                            print("New list's length:", len(numbers))  # Printing new list length.
                            print("\nNew list content:", numbers)  # Printing current list content.

                            ###

                            



                --- Negative indices are legal
                    It may look strange, but negative indices are legal, and can be very useful.

                    An element with an index equal to -1 is the last one in the list.

                    For example:
                    numbers = [111, 7, 2, 1]
                    print(numbers[-1])
                    print(numbers[-2])
                    print(numbers[-3])
                    print(numbers[-4])

                    #The last accessible element in our list is numbers[-4] (the first one) 
                    # ‒ don't try to go any further!


                    Scenario 01:
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).

#code sample
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)





                --- Functions vs. methods
                    A method is a specific kind of function,
                         ‒ it behaves like a function and looks like a function,
                           but differs in the way in which it acts, and in its invocation style.

                    A function doesn't belong to any data,
                         ‒ it gets data, it may create new data and it (generally) produces a result.

                    A method does all these things, but is also able to change the state of a selected entity.

                    A method is owned by the data it works for,
                         while a function is owned by the whole code.

                    This also means that invoking a method requires,
                             some specification of the data from which the method is invoked.

                    It may sound puzzling here, 
                            but we'll deal with it in depth when we delve into object-oriented programming.

                    In general, a typical function invocation may look like this:

                    result = function(arg)
                    
                    The function takes an argument, does something, and returns a result.

                    
                    A typical method invocation usually looks like this:

                    result = data.method(arg)
                    
                    Note: the name of the method is preceded by the name of the data which owns the method.
                            Next, you add a dot, followed by the method name, and a pair of parenthesis,
                                 enclosing the arguments.

                    The method will behave like a function, but can do something more,
                             ‒ it can change the internal state of the data from which it has been invoked.

                             


                --- Adding elements to a list: append() and insert()
                    01. append()
                            It takes its argument's value and puts it at the end of the list which owns the method.

                            list.append(value)

                    02. insert()
                            adds a new element at any place in the list, not only at the end.

                            list.insert(location, value)

                            It takes two arguments:

                            - the first shows the required location of the element to be inserted;
                                 note: all the existing elements that occupy locations,
                                     to the right of the new element (including the one at the indicated,
                                       position) are shifted to the right, in order to make space for the new,
                                         element;
                            - the second is the element to be inserted.

                            For example:
                                numbers = [111, 7, 2, 1]
                                print(len(numbers))
                                print(numbers)

                                ###

                                numbers.append(4)

                                print(len(numbers))
                                print(numbers)

                                ###

                                numbers.insert(0, 222)
                                print(len(numbers))
                                numbers.insert(1, 333)

                                print(numbers)

                                #


                                You can start a list's life by making it empty,
                                     (this is done with an empty pair of square brackets),
                                                 and then adding new elements to it as needed.
                                For example:
                                    my_list = []  # Creating an empty list.

                                    for i in range(5):
                                        my_list.append(i + 1)

                                    print(my_list)

                                For example02:
                                my_list = []  # Creating an empty list.

                                for i in range(5):
                                    my_list.insert(0, i + 1)

                                print(my_list)






                --- Making use of lists
                    In for loop
                    
                    For example
                    my_list = [10, 1, 8, 3, 5]
                    total = 0

                    for i in range(len(my_list)):
                        total += my_list[i]

                    print(total)


                    For example:
                    my_list = [10, 1, 8, 3, 5]
                    total = 0

                    for i in my_list:
                        total += i

                    print(total)

                    What happens here?

                    the for instruction specifies the variable used to browse the list (i here) followed by the in keyword and the name of the list being processed (my_list here)
                    the i variable is assigned the values of all the subsequent list's elements, and the process occurs as many times as there are elements in the list;
                    this means that you use the i variable as a copy of the elements' values, and you don't need to use indices;
                    the len() function is not needed here, either.



                    

                --- Lists in action
                    Imagine that you need to rearrange the elements of a list, 
                            i.e., reverse the order of the elements:

                        variable_1 = 1
                        variable_2 = 2

                        variable_2 = variable_1
                        variable_1 = variable_2

                        If you do something like this, you would lose the value previously stored in variable_2.
                                 Changing the order of the assignments will not help. 
                                        You need a third variable that serves as an auxiliary storage.

                        This is how you can do it:

                        variable_1 = 1
                        variable_2 = 2

                        auxiliary = variable_1
                        variable_1 = variable_2
                        variable_2 = auxiliary

                        Python offers a more convenient way of doing the swap – take a look:

                        variable_1 = 1
                        variable_2 = 2

                        variable_1, variable_2 = variable_2, variable_1


                        Clear, effective and elegant - isn't it?

                        Now you can easily swap the list's elements to reverse their order:


                        my_list = [10, 1, 8, 3, 5]

                        my_list[0], my_list[4] = my_list[4], my_list[0]
                        my_list[1], my_list[3] = my_list[3], my_list[1]

                        print(my_list)



                --- LAB
                    Scenario
The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.

##Code
# step 1
beatles = [ ]
print("Step 1:", beatles)

# step 2
print("Step 2:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 3
print("Step 3:", beatles)
for members in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(members)

# step 4
print("Step 4:", beatles)
del beatles[3]
del beatles[3]

# step 5
print("Step 5:", beatles)
beatles.insert(0, "Ringo Starr")

# testing list legth
print("The Fab", len(beatles))
print(beatles)



#SECTION SUMMARY

1. The list is a type of data in Python used to store multiple objects. It is an ordered and mutable collection of comma-separated items between square brackets, e.g.:


my_list = [1, None, True, "I am a string", 256, 0]
 
2. Lists can be indexed and updated, e.g.:


my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0
 
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
 
my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
 
3. Lists can be nested, e.g.:


my_list = [1, 'a', ["list", 64, [0, 1], False]]
 
You will learn more about nesting in module {{_moduleNumber}}.7 ‒ for the time being, we just want you to be aware that something like this is possible, too.

4. List elements and lists can be deleted, e.g.:


my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]
 
del my_list  # deletes the whole list
 
Again, you will learn more about this in module {{_moduleNumber}}.6 ‒ don't worry. For the time being just try to experiment with the above code and check how changing it affects the output.

5. Lists can be iterated through using the for loop, e.g.:


my_list = ["white", "purple", "blue", "yellow", "green"]
 
for color in my_list:
    print(color)
 
6. The len() function may be used to check the list's length, e.g.:


my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5
 
del my_list[2]
print(len(my_list))  # outputs 4
 
7. A typical function invocation looks as follows: result = function(arg), while a typical method invocation looks like this:result = data.method(arg).



"""
# Step 1: Create an empty list named beatles
beatles = []
print("Step 1:", beatles)

# Step 2: Use append() to add John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3: Use a for loop and append() to add Stu Sutcliffe and Pete Best based on user input
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)
print("Step 3:", beatles)

# Step 4: Use del to remove Stu Sutcliffe and Pete Best from the list
del beatles[3]  # Removing Stu Sutcliffe
del beatles[3]  # Removing Pete Best (now at index 3 after previous deletion)
print("Step 4:", beatles)

# Step 5: Use insert() to add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Final output
print("\nThe final list of Beatles members is:", beatles)
