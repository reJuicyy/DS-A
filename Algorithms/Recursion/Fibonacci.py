def fibonacci(n, dic={}):
    if n == 0: 
        return 0
    if n <= 2: 
        return 1
    
    if n in dic: 
        return dic[n]
    
    dic[n] = fibonacci(n-1, dic) + fibonacci(n-2, dic)
    
    return dic[n]


if __name__ == "__main__":
    from random import randint
    
    val = randint(5, 15)
    
    print(f"val: {val}\nCollatz: {fibonacci(val)}")