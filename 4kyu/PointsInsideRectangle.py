# Task
# A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

# How many points with integer coordinates are located inside the given rectangle (including on its sides)?

# Example
# For a = 6 and b = 4, the output should be 23

# The following picture illustrates the example, and the 23 points are marked green.

#SOLUTION HERE
import numpy as np
import math as m

def rectangle_rotation(a, b):
    
    A = m.floor(a / m.sqrt(2))
    B = m.floor(b / m.sqrt(2))
    
    grid1 = (A // 2 * 2 + 1) * (B // 2 * 2 + 1)
    grid2 = ((A + 1) // 2 * 2) * ((B + 1) // 2 * 2)     
    
    return grid1+grid2

  #coding and coding..