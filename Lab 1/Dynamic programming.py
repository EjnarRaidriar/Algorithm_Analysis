import time
import matplotlib.pyplot as plt

# Dynamic Programming Method
def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

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
plt.title("Fibonacci Power of the Matrix Method")
plt.show()