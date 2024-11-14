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



"""
        ###--- Sorting list
            Sorting:
                 refers to arranging data in a particular format. 
            Sorting algorithm specifies the way to arrange data in a particular order.
              Most common orders are in numerical or lexicographical order.

            The importance of sorting lies in the fact that data searching can be optimized
                     to a very high level, if data is stored in a sorted manner.
                             Sorting is also used to represent data in more readable formats.

                             

            Let's say that a list can be sorted in two ways:

            01. increasing (or more precisely ‒ non-decreasing)
                     ‒ if in every pair of adjacent elements,
                                 the former element is not greater than the latter;
            02. decreasing (or more precisely ‒ non-increasing)
                     ‒ if in every pair of adjacent elements,
                                 the former element is not less than the latter.


                --- The bubble sort:
                    It is a comparison-based algorithm in which each pair of adjacent elements
                                 is compared and the elements are swapped if they are not in order.

                    OR:
                     is a simple sorting algorithm that repeatedly steps through a list,
                             compares adjacent items, and swaps them if they are in the wrong order.
                                    This process is repeated until the list is sorted.


                    For example:
                    my_list = []
                    swapped = True
                    num = int(input("How many elements do you want to sort: "))

                    for i in range(num):
                        val = float(input("Enter a list element: "))
                        my_list.append(val)

                    while swapped:
                        swapped = False
                        for i in range(len(my_list) - 1):
                            if my_list[i] > my_list[i + 1]:
                                swapped = True
                                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

                    print("\nSorted:")
                    print(my_list)

                    




                    Real-Life Scenario: Sorting Books by Height
Imagine you have a row of books lined up on a shelf,
 and you want to arrange them by height from shortest to tallest.
   You could start at one end of the row, compare each book with the one next to it,
     and swap them if they are out of order. You'd go through the row multiple times,
       each time moving the taller books towards the end of the row and the shorter ones towards the beginning. After several passes, the books would eventually end up in order from shortest to tallest.

This is essentially how bubble sort works: 
it repeatedly moves the largest element to the end of the list in each pass, 
"bubbling" the largest elements up.

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Track if any swaps happen
        swapped = False
        # Last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break
    return arr

# Example usage
books = [5, 2, 9, 1, 5, 6]  # List of book heights
sorted_books = bubble_sort(books)
print("Sorted book heights:", sorted_books)





Python, however, has its own sorting mechanisms. No one needs to write their own sorts, 
as there is a sufficient number of ready-to-use tools.

result = data.sort()

For example:
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)


                        --- Operation on lists
                        feature of lists, which strongly distinguishes them from ordinary variables.
                        Example:
                        list_1 = [1]
                        list_2 = list_1
                        list_1[0] = 2
                        print(list_2)

                        The program:

                        creates a one-element list named list_1;
                        assigns it to a new list named list_2;
                        changes the only element of list_1;
                        prints out list_2.


                        Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.

                        You could say that:

                        the name of an ordinary variable is the name of its content;
                        the name of a list is the name of a memory location where the list is stored.
                        Read these two lines once more ‒ the difference is essential for understanding,
                                 what we are going to talk about next.

                        The assignment: list_2 = list_1 copies the name of the array, not its contents.
                             In effect, the two names (list_1 and list_2) identify the same location in the computer memory.
                                     Modifying one of them affects the other, and vice versa.

                        Fortunately, the solution is at your fingertips ‒ it's called a slice.

                        list_1 = [1]
                        list_2 = list_1[:]
                        list_1[0] = 2
                        print(list_2)

                        




                        ---# SECTION SUMMARY #---
                        1. If you have a list list_1, then the following assignment:
                             list_2 = list_1 does not make a copy of the list_1 list, 
                                but makes the variables list_1 and list_2 point to one and the same list in memory.
                                  For example:

                            vehicles_one = ['car', 'bicycle', 'motor']
                            print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']
                            
                            vehicles_two = vehicles_one
                            del vehicles_one[0] # deletes 'car'
                            print(vehicles_two) # outputs: ['bicycle', 'motor']
                            


                            2. If you want to copy a list or part of the list, 
                            you can do it by performing slicing:

                                colors = ['red', 'green', 'orange']
                                
                                copy_whole_colors = colors[:]  # copy the entire list
                                copy_part_colors = colors[0:2]  # copy part of the list
                                

                                3. You can use negative indices to perform slices, too. For example:

                                sample_list = ["A", "B", "C", "D", "E"]
                                new_list = sample_list[2:-1]
                                print(new_list)  # outputs: ['C', 'D']
                                


                                4. The start and end parameters are optional when performing a slice:
                                     list[start:end], e.g.:

                                my_list = [1, 2, 3, 4, 5]
                                slice_one = my_list[2: ]
                                slice_two = my_list[ :2]
                                slice_three = my_list[-2: ]
                                
                                print(slice_one)  # outputs: [3, 4, 5]
                                print(slice_two)  # outputs: [1, 2]
                                print(slice_three)  # outputs: [4, 5]
                                


                                5. You can delete slices using the del instruction:

                                my_list = [1, 2, 3, 4, 5]
                                del my_list[0:2]
                                print(my_list)  # outputs: [3, 4, 5]
                                
                                del my_list[:]
                                print(my_list)  # deletes the list content, outputs: []
                                


                                6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:

                                my_list = ["A", "B", 1, 2]
                                
                                print("A" in my_list)  # outputs: True
                                print("C" not in my_list)  # outputs: True
                                print(2 not in my_list)  # outputs: False




                               ---# Multidimensional nature of lists: advanced applications #---
Let's go deeper into the multidimensional nature of lists. To find any element of a two-dimensional list, you have to use two coordinates:

a vertical one (row number)
and a horizontal one (column number).
Imagine that you're developing a piece of software for an automatic weather station. The device records the air temperature on an hourly basis and does it throughout the month. This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

First, you have to decide which data type would be adequate for this application. In this case, a float would be best, since this thermometer is able to measure the temperature with an accuracy of 0.1 ℃.

Then you take an arbitrary decision that the rows will record the readings every hour on the hour (so the row will have 24 elements) and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days, so you need 31 rows). Here's the appropriate pair of comprehensions (h is for hour, d for day):


temps = [[0.0 for h in range(24)] for d in range(31)]
 
The whole matrix is filled with zeros now. You can assume that it's updated automatically using special hardware agents. The thing you have to do is to wait for the matrix to be filled with measurements.

Now it's time to determine the monthly average noon temperature. Add up all 31 readings recorded at noon and divide the sum by 31. You can assume that the midnight temperature is stored first. Here's the relevant code:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Average temperature at noon:", average)
 
Note: the day variable used by the for loop is not a scalar ‒ each pass through the temps matrix assigns it with the subsequent rows of the matrix; hence, it's a list. It has to be indexed with 11 to access the temperature value measured at noon.

Now find the highest temperature during the whole month ‒ see the code:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)
 
Note:

the day variable iterates through all the rows in the temps matrix;
the temp variable iterates through all the measurements taken in one day.
Now count the days when the temperature at noon was at least 20 ℃:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "days were hot.")
 
Python does not limit the depth of list-in-list inclusion. Here you can see an example of a three-dimensional array:


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.

First step ‒ the type of the array's elements. In this case, a Boolean value (True/False) would fit.

Step two ‒ calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.

Now you can create the array:


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.

Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:


rooms[1][9][13] = True
 
and release the second room on the fifth floor located in the first building:


rooms[0][4][1] = False
 
Check if there are any vacancies on the 15th floor of the third building:


vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
 
The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.
                                
"""