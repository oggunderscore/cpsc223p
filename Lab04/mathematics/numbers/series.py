def sum_values(nums = None):
    total = 0
    for value in nums:
        total += value
    return total

def average_values(nums = None):
    if len(nums) == 0:
        return 0 

    total = sum(nums)
    average = total / len(nums)
    return average