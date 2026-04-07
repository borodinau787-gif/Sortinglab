import random

def binary_search(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        elif arr[mid] > val:
            end = mid - 1
        else:
            return mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(20)]
    print("Original:", *data)
    print("Binary Sort:", *binary_insertion_sort(data.copy()))