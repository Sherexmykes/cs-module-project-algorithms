'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    resulted_array = []
    
    for i in range(len(nums)-(k-1)):
        end = i + k
        window = nums[i:end]
        max_num = max(window)
        resulted_array.append(max_num) 
        
    return resulted_array
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print( {sliding_window_max(arr, k)})
