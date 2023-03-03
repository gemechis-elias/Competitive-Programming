def superDigit(n, k):
    
    if len(n) == 1:
        return n
    my_sum = 0
    if k > 0:
        for i in n:
            my_sum += int(i)
        my_sum *= k
        k = 0
    else:
        for i in n:
            my_sum += int(i)
            
    
    return superDigit(str(my_sum), k
