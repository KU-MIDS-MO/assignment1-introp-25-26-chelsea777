def is_strictly_increasing_digits(n):
    ### Replace with your own code (begin) ###
    if type(n)!=int or n <0:
        return -1
    if n < 10:
        return True
    
    last = 10
    while n > 0:
        d= n%10
        if d>=last:
            return False
        last = d
        n //=10
    return True
    




    ### Replace with your own code (end)   ###