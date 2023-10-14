def max_of_three_num(a,b,c):
    if a > b:
        if a > c:
            return a
        return c
    else:
        if b > c:
            return b
        return c
    
print(max_of_three_num(13,52,6))