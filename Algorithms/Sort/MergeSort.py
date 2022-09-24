def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    
    mid = len(seq)//2
    
    return merge(merge_sort(seq[:mid]), merge_sort(seq[mid:]))

def merge(left_seq, right_seq):
    l = r = 0
    k = 0
    
    seq = left_seq + right_seq
    
    while l < len(left_seq) and r < len(right_seq):
        if left_seq[l] <= right_seq[r]:
            seq[k] = left_seq[l]
            l += 1
        else:
            seq[k] = right_seq[r]
            r += 1
        k += 1
    
    while l < len(left_seq):
        seq[k] = left_seq[l]
        l += 1
        k += 1
    
    while r < len(right_seq):
        seq[k] = right_seq[r]
        r += 1
        k += 1
    
    return seq


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {merge_sort(lst)}")