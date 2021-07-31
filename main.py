import math
import matplotlib.pyplot as plt



x = float(input("What radians would you like to calulate?: "))
n = 80
def iteration(i):
    return (((-1)**i) * (x**((2*i)+1))) / math.factorial((2*i)+1)

def mainFunction(n,x):
    answer = 0
    for i in range (0,n):
        answer += iteration(i)
    
    return answer


def accuracyGrapher():
    xValues = []
    yValues = []
    numberOfNsToCheck = n
    for j in range(0,numberOfNsToCheck):
        accuracy = math.sin(x) - mainFunction(j,x)
        xValues.append(j)
        yValues.append(accuracy)
    
    plt.plot(xValues, yValues)
    plt.ylabel('error')
    plt.xlabel('N approximations')
    plt.show()

accuracyGrapher()


print(mainFunction(n,x))
print(math.sin(x))

