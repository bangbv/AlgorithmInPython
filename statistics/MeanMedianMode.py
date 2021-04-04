import statistics
from statistics import mode

array = input()

m_input = [int(elem) for elem in array.split()]
print(sum(m_input)/len(m_input))

arr_sorted = sorted(m_input)
l = len(arr_sorted)
m = l//2
if l%2:
  print(arr_sorted[m])
else:
  print(sum(arr_sorted[m-1:m+1])/2)

from collections import Counter

# list of elements to calculate mode
n_num = arr_sorted
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
get_mode = mode[0]

print(get_mode)