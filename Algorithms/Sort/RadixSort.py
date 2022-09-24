from math import log10, ceil
from functools import reduce


def radix_sort(seq):
    if len(seq) <= 1: 
        return seq
    
    k = ceil(log10(max(seq)))
    
    for dig in range(k):
        digit_list = [[] for _ in range(10)]
        for elem in seq:
            num = elem // 10 ** dig % 10
            digit_list[num].append(elem)
        seq = flatten(digit_list)
            
    return seq

def flatten(seq):
    return reduce(lambda x, y: x + y, seq)


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {radix_sort(lst)}")