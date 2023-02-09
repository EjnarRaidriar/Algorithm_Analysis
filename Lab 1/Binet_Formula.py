import decimal
import time
import matplotlib.pyplot as plt
import math


def fib(n):
    phi = (1 + math.sqrt(5)) / 2

    return round(decimal.Decimal(pow(decimal.Decimal(phi), decimal.Decimal(n))) / decimal.Decimal(math.sqrt(5)))


# Store the time taken to calculate each Fibonacci number
times = []
fib_numbers = [
    501, 631, 794, 1000, 1259, 1585, 1995,
    2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

for i in fib_numbers:
    start_time = time.time()
    temp = fib(i)
    end_time = time.time()
    times.append(end_time - start_time)
    print(i, end_time - start_time)

# Plot the results
plt.plot(fib_numbers, times, color='blue', marker='.', linestyle='solid', markerfacecolor='black')
plt.xlabel("Fibonacci n-th term")
plt.ylabel("Time (s)")
plt.title("Fibonacci Binet Formula")
plt.show()
