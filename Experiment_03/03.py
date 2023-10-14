def check_num(num):
    
    def factorial(a):
        if(a==0 or a==1):
            return 1
        return a*factorial(a-1)
    if num < 0 :
        print('the number is negative')
        return 'There is no factorial for negative number'
    elif num > 0:
        print('the number is positive')
        return factorial(num)
    else :
        print('the number is zero')
        return 0
print(check_num(-1))
print(check_num(0))
print(check_num(5))