# Here is a series of functions which implemented under "Divide and conquer" strategy.
# "Divide and conquer" is a method of dividing a problem into smaller sub-problems.
# It uses recursion to divide the problem into sub-problems.
# Base case should be a simplest sub-problem.

# 1. Function which sums all the elements in the array with using recursion
def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


# res = sum([2, 4, 6])
# print(res)


# 2. Function which counts all the elements in the array with using recursion
def count_all(arr):
    if arr == []:
        return 0
    return 1 + count_all(arr[:-1])


# res = count_all([1, 2, 3, 4, 5])
# print(res)


# 3. Function which finds the maximum number in the array with using recursion
def find_max(arr):
    if len(arr) == 0:
        return 0

    # With using max function:
    # return max(arr[0], find_max(arr[1:]))

    # Without using max function:
    max_of_rest = find_max(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


# res = find_max([10, 2, 3, 4, 5])
# print(res)
