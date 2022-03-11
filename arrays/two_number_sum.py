def twoNumberSum(array, targetSum):
    mem = {}
    for num in array:
        if targetSum - num in mem:
            return [num, targetSum - num]
        mem[num] = 1
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))
