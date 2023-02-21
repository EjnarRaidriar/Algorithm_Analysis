import time
import matplotlib.pyplot as plt
import numpy as np
from QuickSort import quickSort
from MergeSort import mergeSort
from HeapSort import heapSort
from TimeSort import timeSort

# random array with 1000 int values >1 and <1000000
randData = np.random.randint(1, 100000, 500)
sortedData = []

times = []

print("QuickSort time")
qSortData = randData
start_time = time.time()
quickSort(qSortData, 0, len(qSortData) - 1)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("random data: " + str(times[0]))
start_time = time.time()
quickSort(qSortData, 0, len(qSortData) - 1)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("sorted data: " + str(times[1]) + "\n")

print("MergeSort time")
mSortData = randData
start_time = time.time()
mergeSort(mSortData)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("random data: " + str(times[2]))
start_time = time.time()
mergeSort(mSortData)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("sorted data: " + str(times[3]) + "\n")

print("HeapSort time")
hSortData = randData
start_time = time.time()
heapSort(hSortData)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("random data: " + str(times[4]))
start_time = time.time()
heapSort(hSortData)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("sorted data: " + str(times[5]) + "\n")

print("TimeSort time")
tSortData = randData
start_time = time.time()
timeSort(tSortData)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("random data: " + str(times[6]) + "\n")
start_time = time.time()
timeSort(tSortData)
end_time = time.time()
times.append(round(end_time - start_time, 6))
print("sorted data: " + str(times[7]) + "\n")

# preparing data for graph
sortType = ['random', 'sorted']
time = {
    "QuickSort": (times[0], times[1]),
    "MergeSort": (times[2], times[3]),
    "HeapSort": (times[4], times[5]),
    "TimeSort": (times[6], times[7])
}

x = np.arange(len(sortType))
width = 0.2
multiplier = 0

fig, ax = plt.subplots(constrained_layout=True)

for attribute, measurement in time.items():
    offset = width * multiplier
    rects = ax.bar(x+offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('Time (s)')
ax.set_title('Sorting Algorithms')
ax.set_xticks(x+width, sortType)
ax.legend(loc='upper right')

plt.show()