#by JUNGWOO JANG
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
#x-values are the angles
x = [-40, -20, 0, 20, 40, 60, 80]
#y-values are the distance
y = [65.333, 130, 383.667, 642.667, 717.667, 626, 365.333]
#The Equation
result = np.polyfit(x, y, 2)
eq = np.poly1d(result)
print(eq)
#Asks for the input from user and converts raw_input, which is like a string, to a number.
def the_input():
    while True:
        the_input = raw_input("Please type an angle or press q to quit-->")
        if the_input == 'q':
            exit(0)
        try:
            number = float(the_input)
        except ValueError:
            print('BIG ERROR, BIG ERROR')
            continue
        print(eq(number))
the_input()
