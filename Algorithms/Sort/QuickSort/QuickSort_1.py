def quick_sort(seq, l, r):
    if len(seq) <= 1:
        return seq
    
    if l < r:
        partition = partitioning(seq, l, r)
        quick_sort(seq, l, partition)
        quick_sort(seq, partition+1, r)
    
    return seq

def partitioning(seq, l, r):
    pivot = seq[l]
    
    while True:
        while seq[r] > pivot:
            r -= 1
        while seq[l] < pivot:
            l += 1
            
        if l >= r:
            return r
        
        seq[l], seq[r] = seq[r], seq[l]
        l, r = l+1, r-1


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {quick_sort(lst, 0, len(lst)-1)}")