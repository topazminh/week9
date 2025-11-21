def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Không tìm thấy

# Demo
arr = [1, 3, 5, 7, 9, 11]
k = 7
pos = binary_search(arr, k)
print("Vị trí:", pos)
