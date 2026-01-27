# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square

#Solution HERE
import math
def find_next_square(sq):
    if sq<0 : 
        return -1
    else : 
        if math.isqrt(sq)**2 != sq :
            return -1
    
    i=math.isqrt(sq)+1
    return i**2
    
        
