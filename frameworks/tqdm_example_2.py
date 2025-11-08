import time
from tqdm import tqdm


if __name__ == '__main__':
    arrays = [1,2,3]
    strs = ['a', 'b', 'c']
    names = ['Apple', 'Tree', 'Hat']

    for i, a, str, name in tqdm(
            (range(len(arrays)), arrays, strs, names)):
        print(f"pair {i}: {a}, {str}, {name}")




