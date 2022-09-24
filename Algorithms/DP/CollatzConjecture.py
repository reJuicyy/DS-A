def collatz(n, k=[]):
    k.append(n)
    
    if n <= 1: 
        return k
    
    if n%2==0: 
        return collatz(n//2, k)
    else: 
        return collatz(3*n+1, k)
    
    
if __name__ == "__main__":
    from random import randint
    
    val = randint(5, 15)
    
    print(f"val: {val}\nCollatz: {collatz(val)}")