def search_recur(arr, x, left, right):
    if left <= right:
        mid = int((left + right) / 2)
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        return search_recur(arr, x, left, right)
    else:
        return -1


def search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print("Hello World")
    arr = [1, 2, 4, 6, 8, 9]
    result = search_recur(arr, 9, 0, len(arr))
    print("result:", result)
