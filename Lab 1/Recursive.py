import time
import matplotlib.pyplot as plt

# Recursive method
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

times = []
fib_numbers = [
    5, 7, 10, 12, 15, 17, 20,
    22, 25, 27, 30, 32, 35, 37, 40, 42]

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