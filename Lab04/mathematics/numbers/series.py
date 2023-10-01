def sum_values(**kwargs):
    values = list(kwargs.values())
    
    if not values:
        return 0  
    
    return sum(values)

def average_values(**kwargs):
    values = list(kwargs.values())
    
    if not values:
        return 0  
    
    return sum(values) / len(values)
