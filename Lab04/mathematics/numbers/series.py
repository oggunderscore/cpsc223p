def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total

def average_values(*args):
    if len(args) == 0:
        return 0 

    total = sum(args)
    average = total / len(args)
    return average