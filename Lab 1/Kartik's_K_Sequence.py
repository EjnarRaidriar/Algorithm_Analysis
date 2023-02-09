import time
import matplotlib.pyplot as plt


def fib(n):
    if n > 0:
        n1, n2 = 1, 1
        if n > 3:
            for _ in range((n//3)):
                n1, n2 = n2, (n2 << 2)+n1  # << 2   is multiply by 4
        if n % 3 == 0:
            return n1
        elif n % 3 == 1:
            return (n2-n1) >> 1  # >> 1   is divide by 2  'F1'
        elif n % 3 == 2:
            return (n2+n1) >> 1  # >> 1   is divide by 2  'F2'
    else:
        return -1


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
plt.title("Fibonacci Kartik's K sequence Method")
plt.show()
