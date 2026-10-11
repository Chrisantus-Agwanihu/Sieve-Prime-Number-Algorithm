import math

def Sieve(limit):
    numbers = range(2,math.floor(math.sqrt(limit)) + 1) # establishing the real numbers from 2 to √n + 1
    RealNumbers = [True] * (limit + 1) # creates a list of n True boolean values
    if limit < 2: # excludes 0 and 1 from the limit
        print("limit less than 2")
        return 
    base = 0
    for i in numbers: # looks through the values fron 2 to √n
            j = 0
            base = math.pow(i, 2) # creates a base that squares the number of interest (the current value from 2 to √n)
            while base + (i * j) < limit + 1: # makes a loop that finds the multiples of i (i^2, i^2 + i, i^2 + 2i)
                composite = base + (i*j) # variable for the composite number/ multiple of i
                RealNumbers[int(composite)] = False # marks the composite number as "False" in the array of booleans
                j+=1 # increments j so we can find the next multiple
    RealNumbers[0] = False 
    RealNumbers[1] = False # makes sure 0 and 1 are not considered in our table of primes
    print([i for i in range(2, limit + 1) if RealNumbers[i] == True]) # loops through our values from 2 to n and prints the prime numbers labelled as "True"


maximum = int(input("What do you want the maximum to be?: ")) # asks for maximum value

Sieve(maximum)
