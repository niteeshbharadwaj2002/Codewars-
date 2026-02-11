# Intervals
# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

# Overlapping Intervals
# List containing overlapping intervals:

# [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

# Examples:
# sumIntervals( [
#    [1, 2],
#    [6, 10],
#    [11, 15]
# ] ) => 9

# sumIntervals( [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ] ) => 7

# sumIntervals( [
#    [1, 5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ] ) => 19

# sumIntervals( [
#    [0, 20],
#    [-100000000, 10],
#    [30, 40]
# ] ) => 100000030
# Tests with large intervals
# Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range [-1000000000, 1000000000].

#SOLUTION HERE
def sorted_number(intervals):
    sorted = []
    for i in range(len(intervals)):
        for j in range(len(intervals[i])):
            if(j==0):
                sorted.append((intervals[i][j], 's'))
            elif(j==len(intervals[i])-1):
                sorted.append((intervals[i][j], 'e'))
            else: sorted.append((intervals[i][j], ''))
    sorted.sort()
    return sorted

def remove_nested_intervals(sorted):
    result = []
    depth = 0
    
    for val, tag in sorted:
        if tag == 's':
            if depth == 0:
                result.append((val, tag))
            depth += 1
        elif tag == 'e':
            depth -= 1
            if depth == 0:
                result.append((val, tag))
                
    return result

def add_intervals(sorted):
    sum = 0
    for i in range(0,len(sorted)-1, 2):
        sum += sorted[i+1][0]-sorted[i][0]
    return sum
def sum_of_intervals(intervals):
    sorted = sorted_number(intervals)     
    sorted = remove_nested_intervals(sorted)
    sum = add_intervals(sorted)
    return sum