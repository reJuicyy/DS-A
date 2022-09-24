def selection_sort(seq):
    if len(seq) <= 1: 
        return seq
    
    for i in range(len(seq)):
        s_index = i
        for j in range(s_index+1, len(seq)):
            if seq[s_index] > seq[j]: 
                s_index = j
        seq[i], seq[s_index] = seq[s_index], seq[i]
    
    return seq


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {selection_sort(lst)}")