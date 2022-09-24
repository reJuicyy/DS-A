def insertion_sort(seq):
    if len(seq) <= 1: 
        return seq
    
    for i in range(1, len(seq)):
        curr = seq[i]
        s_index = i
        while s_index > 0 and seq[s_index-1] > curr:
            seq[s_index] = seq[s_index-1]
            s_index -= 1
        seq[s_index] = curr
        
    return seq


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {insertion_sort(lst)}")