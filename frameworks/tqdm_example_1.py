import time
from tqdm import tqdm
import concurrent.futures
from tqdm.contrib.concurrent import process_map

# Tqdm is a Python library that provides us with progress bars and other helpful statistics,
# making it easier to monitor and manage code execution.
def process():
    for i in tqdm(range(10), desc="Processing range"):
        print(f"Processing: {i}")


def process_data(data):
    for i in tqdm(range(100), desc=f"Processing {data['name']}"):
        # Process data
        time.sleep(0.01)


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = process_map(process_data, [
            {'name': 'dataset1'},
            {'name': 'dataset2'},
        ])
