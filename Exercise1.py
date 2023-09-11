# Problem - Instance
# Input: L = [5, 7, 8, 2, 4]
# Output: 8

# PsuedoCode
# max = List[0]
# for each element in List
#   if max < currentElement
#       set max to that element
# return max


# Implementation
def findMax(list):
    max = list[0]
    for num in list:  # This will compare the first element to itself
        if max < num:
            max = num
    return max


def main():
    testList = [5, 7, 8, 2, 4]
    print("Max Num: " + str(findMax(testList)))


main()

# stepCount 2N
# Space = 0[1]
# Time Complexity = O(n)
# Order of growth = Linear
