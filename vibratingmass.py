import math
import matplotlib.pyplot as plt
import numpy as np

# Program Settings

n = 10
x0 = -4  # Start displacement
xDot0 = 5  # Start velicoty
k = 40
m = 10
c = 5
wn = math.sqrt(k / m)


# Function that takes in X returns Cos(X)

def sinXiteration(i, x):
    return (-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1)


def sinX(n, x):
    answer = 0
    for i in range(0, n):
        answer += sinXiteration(i, x)

    return answer


# Function that takes in X retrunes Cos(x

def cosXiteration(i, x):
    return (-1) ** i * x ** (2 * i) / math.factorial(2 * i)


def cosX(n, x):
    answer = 0
    for i in range(0, n):
        answer += cosXiteration(i, x)

    return answer


# Position and velocity calculation

def position(t):
    return x0 * math.cos(wn * t) + xDot0 / wn * math.sin(wn * t)


def velocity(t):
    return -x0 * wn * math.sin(wn * t) + xDot0 * math.cos(wn * t)


# Position and velocity grapher

def positionGrapher():
    xValues = []
    yValues = []
    yValuesVelocity = []
    for j in np.linspace(0, 20, 100):
        xValues.append(j)
        yValues.append(position(j))
        yValuesVelocity.append(velocity(j))
    plt.plot(xValues, yValues)
    plt.plot(xValues, yValuesVelocity)
    plt.ylabel('Position')
    plt.xlabel('Time')
    plt.show()


positionGrapher()
