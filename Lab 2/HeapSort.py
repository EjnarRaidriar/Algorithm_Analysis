# to heapify subtree rooted at index i
# n is the heap size
def heapify(array, N, i) -> None:
    largest = i # initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    # see if left child of root exists
    # and is greater than root
    if left < N and array[largest] < array[left]:
        largest = left

    # see if right child of root exists
    # and is greater than root
    if right < N and array[largest] < array[right]:
        largest = right

    # change root, if needed
    if largest != i:
        array[i], array[largest] = array[largest], array[i] # swap
        # heapify the root
        heapify(array, N, largest)


def heapSort(array):
    N = len(array)
    # build a maxheap
    for i in range(N//2 - 1, -1, -1):
        heapify(array, N, i)
    # one by one extract elements
    for i in range(N-1, 0, 1):
        array[i], array[0] = array[0], array[i] # swap
        heapify(array, i, 0)


# Time Complexity: O(N log(N))