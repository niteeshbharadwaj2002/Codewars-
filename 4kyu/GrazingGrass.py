# The King and Queen of FarFarAway are 
# going to pay Shrek and Fiona a visit at their swamp.
# However, Shrek is afraid that Donkey is going to be naughty again, 
# so he decides to tie him up so he will not disturb the royal dinner. 
# Shrek grows a circular patch of delicious grass, 
# and decides to rope Donkey to a fence post on its border. 
# However he's afraid that when Donkey gets hungry, '
# 'he will eat all the grass, and Shrek needs the grass to prepare '
# 'a dish of tasty ogre grass salad for the dinner. '
# 'The rope needs to be short, so Donkey won't be able to eat (or, even worse, fertilize) 
# too much grass.

# Grass patch

# Given the diameter of the circular grass patch (measured in ogre steps), 
# calculate the maximum length of the rope so Donkey won't be able to eat 
# more than given percentage of grass (given as ratio in range 0 <= percentage <= 1, i.e. 0.5 means 50%). 
# As Shrek is just an ogre and is not really familiar with fractions, the length should be returned as whole ogre steps. 
# Beware: in the Fairy Land, grass patches can grow very large!

#SOLUTION HERE
import math as m
def get_rope_length(D, p):
    
    if(p<=0 or D<=0): return 0.0
    elif(p>=1): return float(D)

    R = D/2
    A = m.floor(m.pi * (R**2))
    
    arc_area = A * p
    
    low = 0.0
    high = float(D)
    
    for _ in range(100):
        r = (low + high) / 2.0
        
        # Clamp the value for acos to prevent Domain Errors
        cos_val1 = max(-1.0, min(1.0, r / (2 * R)))
        cos_val2 = max(-1.0, min(1.0, 1 - (r**2 / (2 * R**2))))
        
        term1 = r**2 * m.acos(r / (2 * R))
        term2 = R**2 * m.acos(1 - (r**2 / (2 * R**2)))
        term3 = (r / 2) * m.sqrt(4 * R**2 - r**2)
        rhs_area = m.floor(term1 + term2 - term3)
        
        if rhs_area < arc_area:
            low = r
        else:
            high = r
    return int(m.floor(high + 1e-9))