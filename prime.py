import time
import math
import matplotlib.pyplot as plt


# Methods for finding all prime numbers up to max value 'n'
# Slow method using a basic check
def slow_method(n: int) -> list:
    results = [2]
    for i in range(3, n, 2):
        is_prime = True
        for j in range(3, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            results.append(i)
    return results


# Fast method using squares
def fast_method(n: int) -> list:
    results = [2]
    for i in range(3, n, 2):
        is_prime = True
        for j in range(3, int(math.sqrt(i) + 1)):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            results.append(i)
    return results


# Faster method using previous results
def faster_method(n: int) -> list:
    results = [2]
    for i in range(3, n, 2):
        is_prime = True
        limit = math.sqrt(i)
        for j in results:
            if j > limit:
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            results.append(i)
    return results


def main():
    # Graph the methods against each other to show the speed over time
    # Add methods to test into the 'methods' list
    methods = [fast_method, faster_method]
    times = [[] for method in methods]
    # Test all 'n' values from 0 to 100000 in increments of 1000
    n_values = range(0, 100000, 1000)
    for n in n_values:
        # Test each method and record the elapsed time
        for method in methods:
            start_time = time.perf_counter()
            results = method(n)
            elapsed_time = time.perf_counter() - start_time
            times[methods.index(method)].append(elapsed_time)
            print(f"Method '{method.__name__}' found \t{len(results)} primes in \t{elapsed_time} seconds")
    # Graph elapsed time for each method
    for method in methods:
        plt.plot(n_values, times[methods.index(method)], label=method.__name__)
    plt.legend()
    plt.xlabel("n")
    plt.ylabel("seconds")
    plt.show()


if __name__ == '__main__':
    main()
