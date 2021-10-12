# Test the difference in accuracy between sin() and Python's math.sin()
import math
import matplotlib.pyplot as plt


# Calculate sine of 'x' with 'n' iterations
def sin(x: float, n: int) -> float:
    result = 0
    for i in range(0, n):
        result += (-1 ** i) * (x ** ((2 * i) + 1)) / math.factorial((2 * i) + 1)
    return result


# Graph the accuracy difference between 'math.sin(x)' and 'sin(x, n)'
def main(x: float, n: int):
    iterations = []
    results = [[], []]
    for i in range(0, n):
        a = math.sin(x)
        b = sin(x, i)
        iterations.append(i)
        results[0].append(a)
        results[1].append(b)
        print(f"Iteration: {i}")
        print(f"\tmath.sin(x) = \t{a}")
        print(f"\tsin(x, {i}) = \t{b}")
        print(f"\tdifference = \t{a - b}\n")
    plt.plot(iterations, results[1], label="sin(x, n)")
    plt.plot(iterations, results[0], label="math.sin(x)")
    plt.xlabel("iterations")
    plt.ylabel("result")
    plt.legend()
    plt.show()


x = float(input("Radians: "))  # Radians
n = 80  # Iterations
# Over 85 iterations results in OverflowError

if __name__ == '__main__':
    main(x, n)
