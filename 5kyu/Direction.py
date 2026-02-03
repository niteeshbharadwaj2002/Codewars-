# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]

#SOLUTION HERE
def dir_reduc(arr):
    length=len(arr)
    while True:
        pair=False
        for i in range(0,length-1):
            if(arr[i]=="NORTH" and arr[i+1]=="SOUTH"):
                pair=True
                arr.pop(i+1)
                arr.pop(i)
                break
            elif(arr[i]=="SOUTH" and arr[i+1]=="NORTH"):
                pair=True
                arr.pop(i+1)
                arr.pop(i)
                break
            elif(arr[i]=="EAST" and arr[i+1]=="WEST"):
                pair=True
                arr.pop(i+1)
                arr.pop(i)
                break
            elif(arr[i]=="WEST" and arr[i+1]=="EAST"):
                pair=True
                arr.pop(i+1)
                arr.pop(i)
                break
            else: 
                pass
        if(pair==False): 
            break
        length=length-2
        
    return arr           
                
                