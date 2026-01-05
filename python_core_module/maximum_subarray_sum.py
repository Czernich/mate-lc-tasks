# Task: Write a function that finds the contiguous subarray with the largest sum.
# Return the sum of that subarray.
# Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])

def max_subarray_sum(nums: list) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), expected_result=6)
    validate_response(result=max_subarray_sum([1]), expected_result=1)
    validate_response(result=max_subarray_sum([5, 4, -1, 7, 8]), expected_result=23)
    validate_response(result=max_subarray_sum([-1, -2, -3]), expected_result=-1)
    validate_response(result=max_subarray_sum([1, 2, 3, 4]), expected_result=10)
    validate_response(result=max_subarray_sum([-2, -1]), expected_result=-1)

# Solution

def max_subarray_sum(nums: list) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum