
def quicksort(list, low, high):
    if low >= high:
        return None
    left = low
    right = high
    key = list[low]
    while left < right:
        while list[right] >= key and left < right:                      #从后向前查找
            right = right - 1
        list[left] = list[right]
        while list[left] <= key and left < right:
            left = left + 1
        list[right] = list[left]
    list[left] = key
    quicksort(list, low, left-1)
    quicksort(list, left+1, high)
    return list
list = [6, 2, 7, 3, 8, 9]
print(quicksort(list, 0, len(list)-1))