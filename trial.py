import itertools
import math
all_combinations = []
sums = sum(7, 6)
lists = [7, 4, 6, 7, 20, 249]
for i in range(len(lists)):
    combinations_object = itertools.combinations(lists, i)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list
for sums in all_combinations:
    if sum(sums) == k:
        return len(sums)
