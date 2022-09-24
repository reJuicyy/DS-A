def binary_search(seq, target, l, r):
    while r >= l:
        mid = r - (r - l) // 2
        if seq[mid] == target:
            return mid
        elif seq[mid] > target:
            r = mid-1
        elif seq[mid] < target:
            l = mid+1
        
    return -1


if __name__ == "__main__":
    from random import randint
    
    lst = [_ for _ in range(50)]
    target = randint(0, 100)
    
    print(f"Target: {target}\nIndex: {binary_search(lst, target, 0, len(lst)-1)}")