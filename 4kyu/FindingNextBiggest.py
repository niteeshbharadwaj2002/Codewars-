# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

#SOLUTION HERE
import math as m
def arr_number(arr):
    sum=0
    j=0
    for i in range(len(arr)-1, -1, -1):
        sum = sum + arr[i]*(10**j)
        j+=1
    return sum
def number_arr(number):
    arr=[]
    cpy=number
    while True:
        if (cpy<10):
            arr.append(cpy)
            break
        arr.append(cpy%10)
        cpy=m.floor(cpy/10)
    reversed_array = arr[::-1]
    return reversed_array

def next_bigger(n):
    
    arr = number_arr(n)
    
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
        
    if i == -1: return -1
    
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
        
    arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1:] = sorted(arr[i+1:])
    
    result = arr_number(arr)
    
    return result
