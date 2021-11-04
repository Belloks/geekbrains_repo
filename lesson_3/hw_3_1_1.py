def div(*args):

    try:
        arg1 = int(input("Enter your number "))
        arg2 = int(input("Enter your divider "))
        res = arg1 / arg2
    except ValueError:
        return 'Please enter a valid number'
    except ZeroDivisionError:
        return "Wrong divider! You can't use zero"

    return res

print(f'Result  {div()}')