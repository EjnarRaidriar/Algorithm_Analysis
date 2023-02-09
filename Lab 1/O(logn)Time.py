import time
import matplotlib.pyplot as plt
# O(log n) time
MAX = 100000

# Create an array for memoization
f = [0] * MAX

# Returns n'th fibonacci number using table f[]
def fib(n):
    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if ((n & 1)):
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]

# Store the time taken to calculate each Fibonacci number
times = []
# fib_numbers = [
#     5, 7, 10, 12, 15, 17, 20,
#     22, 25, 27, 30, 32, 35, 37, 40, 42]
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
plt.title("Fibonacci O(log n) time Method")
plt.show()
