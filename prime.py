import time
import math
import psutil
import matplotlib.pyplot as plt



# ----------------------------------------------------------------------
# Start message
print("Prime Number Finder has started!")
print("This may take a momment...")


# ----------------------------------------------------------------------
# Fast Method using squares
def fastMethod(n):
    start_time = time.time()
    primeNumbersFound = [2]

    for i in range (3, n, 2):
        isPrime = True
        for j in range (3, (int)(math.sqrt(i) + 1)):
            if i % j == 0:
                isPrime = False
                break 
        if isPrime: 
            primeNumbersFound.append(i)
    #print("Prime Numbers Fast")
    #print(len(primeNumbersFound))
    #print("--- %s seconds ---" % (time.time() - start_time))
    fastTime = (time.time() - start_time)
    return fastTime

# ----------------------------------------------------------------------
#Slow Method using a basic check
def slowMethod(n):
    start_time = time.time()
    primeNumbersFoundSlow = []

    for i in range (2, n, 1):
        isPrime = True
        for j in range (2, i, 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime == True:
            primeNumbersFoundSlow.append(i)
    #print("Prime Numbers Slow")
    #print(len(primeNumbersFoundSlow))
    #print("--- %s seconds ---" % (time.time() - start_time))
    slowTime = (time.time() - start_time)
    return slowTime

# ----------------------------------------------------------------------
#Graph the two against eachother, and see the speed over time:

timesSlowMethod = []
cpuUssage = []
timesFastMethod = []
nValues = range (0, 50000, 1000)
for n in nValues:
    timesSlowMethod.append(slowMethod(n))
    timesFastMethod.append(fastMethod(n))
    cpuUssage.append(psutil.virtual_memory(1)    
    # Fill the top bound with n, for each function.
    # Store the number of primes found for each at each n
    # Graph two seperate lines. n vs slow, n vs fast.

plt.plot(nValues, timesFastMethod, label = "Fast Method")
plt.plot(nValues, timesSlowMethod, label = "Slow Method")
plt.plot(nValues, cpuUssage, label = 'CPU Ussage')
plt.legend()
plt.xlabel("Size of Primes to Find")
plt.ylabel("Time")
plt.show()


