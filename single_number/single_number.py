'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your Code Here
    #We need to initalize a null list for single integers
    single_list = []
    duplicate_list = []

    # go through all elements
    for element in arr:
        if element not in single_list:
            single_list.append(element)
        else:
            duplicate_list.append(element)
            single_list.remove(element)
    return single_list[0]

    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print({single_number(arr)})
     # had to get rid of f"The odd-number-out is for the test to run