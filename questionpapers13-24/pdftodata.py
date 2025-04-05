def quick_sort(array, start, end):
    if end <= start:
        return  # Base case
    
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)

def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    i += 1
    array[i], array[end] = array[end], array[i]
    
    return i
array = [2, 8, 5, 3, 9, 4, 7, 6, 1]

quick_sort(array, 0, len(array) - 1)    
for i in array:
        print(i, end=" ")
