def fibonacci_search(seq, target):
    fibMm2, fibMm1 = 0, 1
    fibM = fibMm1 + fibMm2
    
    while fibM < len(seq):
        fibMm2 = fibMm1
        fibMm1 = fibM
        fibM = fibMm2 + fibMm1
        
    offset = -1
    
    while fibM > 1:
        i = min(offset + fibM, len(seq)-1)
        
        if seq[i] == target:
            return i
        elif seq[i] < target:
            fibM = fibMm1
            fibMm1 = fibMm2
            fibMm2 = fibM - fibMm1
            offset = i
        elif seq[i] > target:
            fibM = fibMm2
            fibMm1 = fibMm1 - fibMm2
            fibMm2 = fibM - fibMm1
    
    if  fibMm1 and seq[len(seq)-1] == target:
        return len(seq)-1
    
    return -1


if __name__ == "__main__":
    from random import randint
    
    lst = [_ for _ in range(50)]
    target = randint(0, 100)
    
    print(f"Target: {target}\nIndex: {fibonacci_search(lst, target)}")