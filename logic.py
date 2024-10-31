#Computer Logic
"""
        Computer logic:
                It's clear that Python must have operators to build conjunctions and disjunctions. Without them, 
                the expressive power of the language would be substantially weakened.
                  They're called logical operators.
                  01. and operator:
                        It's a binary operator with a priority that is lower than the one expressed by the comparison operators. 
                        This logical operator is called a conjunction.
                        For example:
                            counter > 0 and value == 100

                        The result provided by the and operator can be determined on the basis of the truth table.
                        False + False = False
                        False + True = False
                        True + False = False
                        True + True = True

                 02. or operator:
                        It's a binary operator with a lower priority than and (just like + compared to *).
                         This logical operator is called a disjunction.
                         True + True = True
                         True + False = True
                         False + True = True
                         False + False = False

                03. not operator:
                        It's a unary operator performing a logical negation.
                                 Its operation is simple: it turns truth into falsehood and falsehood into truth.
                                        This operator is written as the word not, and its priority is very high:
                                          the same as the unary + and -. Its truth table is simple:
                                          False = True
                                          True = False

                Logical expressions:
                not (p and q) == (not p) or (not q)
                not (p or q) == (not p) and (not q)

                Note how the parentheses have been used to code the expressions ‒ we put them there to improve readability.

                We should add that none of these two-argument operators can be used in the abbreviated form known as op=.
                  This exception is worth remembering.




                Bitwise operators:
                        Are four operators that allow you to manipulate single bits of data. 

                        They cover all the operations we mentioned before in the logical context, and one additional operator.
                             This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).

                        Here are all of them:

                        (&) (ampersand) ‒ bitwise conjunction;
                        (|) (bar) ‒ bitwise disjunction;
                        (~) (tilde) ‒ bitwise negation;
                        (^) (caret) ‒ bitwise exclusive or (xor).


                    Let's make it easier:

                          (&) requires exactly two 1s to provide 1 as the result;
                          (|) requires at least one 1 to provide 1 as the result;
                          (^) requires exactly one 1 to provide 1 as the result.
                              Let us add an important remark: the arguments of these operators must be integers;
                                   we must not use floats here.

                          The difference in the operation of the logical and bit operators is important:
                              the logical operators do not penetrate into the bit level of its argument. 
                                  They're only interested in the final integer value.

                          Bitwise operators are stricter: they deal with every bit separately.
                               If we assume that the integer variable occupies 64 bits (which is common in modern computer systems),
                                   you can imagine the bitwise operation as a 64-fold evaluation of the logical operator for each pair of bits of the arguments. 
                                      This analogy is obviously imperfect, 
                                          as in the real world all these 64 operations are performed at the same time (simultaneously).

                  Binary left shift and binary right shift:
                        Python offers yet another operation relating to single bits: shifting. This is applied only to integer values, 
                            and you mustn't use floats as arguments for it.
                            For example:
                             How do you multiply any number by ten?
                             12345 × 10 = 123450

                             As you can see, multiplying by ten is in fact a shift of all the digits to the left and filling the resulting gap with zero.

                             Division by ten?
                             12340 ÷ 10 = 1234

                              Dividing by ten is nothing but shifting the digits to the right.

                              The same kind of operation is performed by the computer, but with one difference:
                                   as two is the base for binary numbers (not 10), 
                                      shifting a value one bit to the left thus corresponds to multiplying it by two;
                                           respectively, shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).

                              The shift operators in Python are a pair of digraphs: << and >>,
                                  clearly suggesting in which direction the shift will act.

                              value << bits
                              value >> bits
                              
                              The left argument of these operators is an integer value whose bits are shifted. 
                                  The right argument determines the size of the shift.

                            For example:
                            var = 17
                            var_right = var >> 1
                            var_left = var << 2
                            print(var, var_left, var_right)
                          Output = 17 68 8
                          Note:

                              17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
                              17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)




                              -*-*-*--  SECTION SUMMARY  --*-*--*
                              1. Python supports the following logical operators:
                                  - and → if both operands are true, the condition is true, e.g., (True and True) is True,
                                  - or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
                                  -  not → returns false if the result is true, and returns true if the result is false,
                                   e.g., not True is False.

                              2. You can use bitwise operators to manipulate single bits of data. The following sample data:
                                  - x = 15, which is 0000 1111 in binary,
                                  - y = 16, which is 0001 0000 in binary.
                                  will be used to illustrate the meaning of bitwise operators in Python.
                                       Analyze the examples below:

                                  - (&) does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
                              |             does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
                                  - (˜)  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
                                  - (^) does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
                                  - (>>) does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
                                  - (<<) does a bitwise left shift, e.g., y << 3 = 128, which is 1000 0000 in binary.

"""

