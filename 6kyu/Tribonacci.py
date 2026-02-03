# Well met with Fibonacci bigger brother, AKA Tribonacci.

# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]

#SOLUTION HERE
def tribonacci(signature, n):
    # If n is 0, return an empty list immediately
    if n == 0:
        return []
    
    # If n is smaller than the signature, return only the first n elements
    if n <= len(signature):
        return signature[:n]
    
    # Create a working copy of the signature
    result = signature[:]
    
    # Continue adding the sum of the last 3 elements until we reach length n
    while len(result) < n:
        # result[-3:] gets the last three items in the list
        next_val = sum(result[-3:])
        result.append(next_val)
    
    return result