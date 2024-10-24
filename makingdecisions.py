"""
        A programmer writes a program and the program asks questions.

        A computer executes the program and provides the answers.
                     The program must be able to react according to the received answers.

        Fortunately, computers know only two kinds of answers:

        01. yes, this is true;
        02. no, this is false.
        You will never get a response like Let me think....,
                             I don't know, or Probably yes, but I don't know for sure.

                To ask questions, Python uses a set of very special operators.
                    01. Comparison: equality operator:(==)equal equal operator
                        To ask this question, you use the == (equal equal) operator.
                                Don't forget this important distinction:

                                (=) is an assignment operator, e.g., a = b assigns a with the value of b;
                                (==) is the question are these values equal? so a == b compares a and b.
                        It is a binary operator with left-sided binding. It needs two arguments and checks if they are equal.

                    02. Equality: the equal to operator (==)
                            The == (equal to) operator compares the values of two operands.
                                 If they are equal, the result of the comparison is True. 
                                    If they are not equal, the result of the comparison is False.
                                            var = 0  # Assigning 0 to var
                                            print(var == 0)

                                            var = 1  # Assigning 1 to var
                                            print(var == 0)

                    
                    03. Inequality: the not equal to operator (!=)
                            The (!=) (not equal to) operator compares the values of two operands, too. Here is the difference:
                                 if they are equal, the result of the comparison is False.
                                     If they are not equal, the result of the comparison is True.
                                            var = 0  # Assigning 0 to var
                                            print(var != 0)

                                            var = 1  # Assigning 1 to var
                                            print(var != 0)


                    04. Comparison operators: greater than (>)
                        black_sheep > white_sheep  # Greater than
                            True confirms it; False denies it.

                    05. Comparison operators: greater than or equal to.(>=)
                        The greater than operator has another special, non-strict variant,
                          but it's denoted differently than in classical arithmetic notation: (>=) (greater than or equal to).
                        There are two subsequent signs, not one.
                        Both of these operators (strict and non-strict), as well as the two others discussed in the next section,
                          are binary operators with left-sided binding, and their priority is greater than that shown by (==) and (!=).
                            For example:
                                    centigrade_outside >= 0.0  # Greater than or equal to


                    
                    06. Comparison operators: less than/less than or equal to (<=)
                        The operators (<) (less than) and its non-strict sibling: (<=) (less than or equal to).
                        For example:
                                current_velocity_mph < 85  # Less than
                                current_velocity_mph <= 85  # Less than or equal to


                    Making use of the answers:
                    There are at least two possibilities: 
                    01. first, you can memorize it (store it in a variable) and make use of it later.
                    02. The second possibility is more convenient and far more common:
                             you can use the answer you get to make a decision about the future of the program.



"""
n = int(input("Enter a number: "))
print(n >= 100)

