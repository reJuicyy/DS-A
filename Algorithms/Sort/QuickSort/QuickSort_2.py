def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    
    mid = len(seq)//2
    pivot = seq[mid]
    
    greater, equal, smaller = [], [], []
    
    for elem in seq:
        if elem == pivot:
            equal.append(elem)
        elif elem > pivot:
            greater.append(elem)
        elif elem < pivot:
            smaller.append(elem)
    
    return quick_sort(smaller) + equal + quick_sort(greater)


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {quick_sort(lst)}")