def count_digits_greater_than(n, t):
    ### Replace with your own code (begin) ###
    if type(n) != int or n<0:
        return -1
    if type(t) !=int or t<0 or t>9:
        return -1
    count = 0
    
    if n==0:
        if 0 > t:
            return 1
        else:
            return 0
        
    while n>0:
        digit = n% 10
        if digit >t:
            count +=1
        n= n // 10
    return count
        
    ### Replace with your own code (end)   ###
