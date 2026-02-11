# Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

# Example:
# countOnes 4 7 should return 8, because:
# 4(dec) = 100(bin), which adds 1 to the result.
# 5(dec) = 101(bin), which adds 2 to the result.
# 6(dec) = 110(bin), which adds 2 to the result.
# 7(dec) = 111(bin), which adds 3 to the result.
# So finally result equals 8.
# WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!

#SOLUTION HERE
def count_in_range(n):
    if n<=0 : 
        return 0
    
    total = n+1
    sum = 0
    bit_pos = 1
    
    while bit_pos <= n :
        
        cycle = bit_pos * 2
        fullcycle = total // cycle
        sum += fullcycle * bit_pos
        reminder = total % cycle
        if reminder > bit_pos:
            sum += (reminder-bit_pos)
        bit_pos *= 2
        
    return sum
    
def count_ones(left, right):
    # Your code here!
    return count_in_range(right) - count_in_range(left-1)