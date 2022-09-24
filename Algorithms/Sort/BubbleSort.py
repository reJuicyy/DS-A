def bubble_sort(seq):
    if len(seq) <= 1: 
        return seq
    
    for i in range(len(seq)-1):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                
    return seq


if __name__ == "__main__":
    from random import randint
    
    lst = [randint(0, 1000) for _ in range(50)]
    
    print(f"Unsorted List: {lst}\nSorted List: {bubble_sort(lst)}")