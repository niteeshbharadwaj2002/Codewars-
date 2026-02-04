# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:

#SOLUTION HERE
import math as m

def snail(snail_map):
    mat_size = len(snail_map)
    snail_path=[]
    
    rows= len(snail_map)
    cols= len(snail_map[0])
    rpath=0
    cpath=0
    count=0
    limit=m.ceil(mat_size/2)
    while True:
        if(count>=limit):break
        
        for i in range(cpath, cols-cpath):
            snail_path.append(snail_map[rpath][i])
        for i in range(rpath + 1, rows-rpath):
            snail_path.append(snail_map[i][cols-cpath-1])
        for i in range(cols-cpath-2, -1+cpath, -1):
            snail_path.append(snail_map[rows-rpath-1][i])
        for i in range(rows-rpath-2, -1+rpath+1, -1):
            snail_path.append(snail_map[i][cpath])
        
        rpath += 1
        cpath += 1
        count += 1
        
    return snail_path