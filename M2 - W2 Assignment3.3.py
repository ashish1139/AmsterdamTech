def sqrt(x) :
    """Returns the square root of a number"""
    try :
        return x ** 0.5
    except :
        print('x must be an int or float')
        
print(sqrt('hello'))
