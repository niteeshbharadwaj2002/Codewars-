# The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

# 1
# 1
# 2² = 4
# 3² = 9
# Can you translate this drawing into an algorithm?

# You will be given two dimensions

# a positive integer length
# a positive integer width
# You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

# Examples in general form:
# (depending on the language)

#   sqInRect(5, 3) should return [3, 2, 1, 1]
#   sqInRect(3, 5) should return [3, 2, 1, 1]
  
#   You can see examples for your language in **"SAMPLE TESTS".**

#SOLUTION HERE
def sq_in_rect(lng, wdth):
    arr=[]
    if (lng==wdth):
        return None
    while True:
        if (lng==1):
            for i in range(wdth): arr.append(1)
            break
        elif (wdth==1):
            for i in range(lng): arr.append(1)   
            break
        else:
            if (lng == wdth):
                arr.append(lng)
                break
            elif (lng < wdth):
                small=min(lng,wdth)
                arr.append(small)
                wdth=wdth-lng
            elif(wdth<lng):
                small=min(lng,wdth)
                arr.append(small)
                lng=lng-wdth
    return arr