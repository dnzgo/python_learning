def binary_search(numbers, target):
    leftIndex = 0
    rightIndex = len(numbers) - 1

    while leftIndex <= rightIndex:

        midIndex = (leftIndex + rightIndex) // 2

        if numbers[midIndex] == target:
            return midIndex
        
        elif numbers[midIndex] > target:
            rightIndex = midIndex - 1

        else:
            leftIndex = midIndex + 1
    
    return -1
    
