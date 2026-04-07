import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


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
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


def measure_performance(size):
    data = [random.randint(1, 100000) for _ in range(size)]

    start_bubble = time.time()
    bubble_sort(data.copy())
    time_bubble = time.time() - start_bubble

    start_binary = time.time()
    binary_insertion_sort(data.copy())
    time_binary = time.time() - start_binary

    print(f"--- Тест для {size} елементів ---")
    print(f"Bubble Sort: {time_bubble:.4f}s")
    print(f"Binary Sort: {time_binary:.4f}s\n")


if __name__ == "__main__":
    sample_20 = [random.randint(1, 100) for _ in range(20)]

    print("Випадкові 20 значень:")
    print(*(sample_20))

    print("\nПісля Bubble Sort (20 значень):")
    print(*(bubble_sort(sample_20.copy())))

    print("\nПісля Binary Sort (20 значень):")
    print(*(binary_insertion_sort(sample_20.copy())))
    print("-" * 30)

    measure_performance(10000)
    measure_performance(20000)