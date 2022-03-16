# Like abs() function in python

def absolute(__x):
    if type(__x) != str:
        if __x > 0:
            return __x

        return __x * -1
    else:
        raise TypeError("bad operand type for: 'str' ")


print(absolute(-1000))
