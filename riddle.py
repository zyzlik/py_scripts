"""
A and B sat in the tree.
A had fallen, B was stolen.
What's remaining in the tree?

Write a program, which reads the two names and outputs the poem, in which these names
are used instead of A and B.

Input format:
Two names, separated by a line break. First name should replace A, second one – B.

Output format:
Three lines of the poem with replaced A and B.
"""

poem = "{A} and {B} sat in the tree.\n"\
       "{A} had fallen, {B} was stolen.\n"\
       "What's remaining in the tree?'"\

print(poem.format(A=input(), B=input()))
