from Search.BinarySearch import search_recur

if __name__ == '__main__':
    print("Hello World")
    arr = [1, 2, 4, 6, 8, 9]
    result = search_recur(arr, 9, 0, len(arr))
    print("result:", result)
