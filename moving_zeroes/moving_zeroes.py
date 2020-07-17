'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    altered_array = []
    zeros = []
    for element in arr:
        if element != 0:
            altered_array.append(element)
        else:
            zeros.append(element)
    altered_array += zeros
    return altered_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print({moving_zeroes(arr)})