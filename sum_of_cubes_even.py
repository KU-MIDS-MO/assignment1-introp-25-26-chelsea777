def sum_of_cubes_even(n):
    ### Replace with your own code (begin) ###
    if type(n) !=int or n <0:
        return -1
    if n>2000:
        print("Warning")
    total = 0
    for i in range(0,n+1,2):
        total += i **3
    return float(total)
    ### Replace with your own code (end)   ###
