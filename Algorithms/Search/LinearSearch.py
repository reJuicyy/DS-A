def linear_search(seq, target):
    for i, elem in enumerate(seq):
        if elem == target:
            return i
        
    return -1


if __name__ == "__main__":
    from random import randint
    
    lst = [_ for _ in range(50)]
    target = randint(0, 100)
    
    print(f"Target: {target}\nIndex: {linear_search(lst, target)}")