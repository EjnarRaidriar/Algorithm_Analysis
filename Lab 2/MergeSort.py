def mergeSort(array) -> None:
    if len(array) > 1:
        # finding the middle of the array
        mid = len(array)//2
        # dividing the array into two halves
        L = array[:mid]
        R = array[mid:]
        # sorting halves
        mergeSort(L)
        mergeSort(R)
        # copy data to temp arrays L[] and R[]
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            array[k] = L[k]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


    # Time Complexity: O(N log(N))