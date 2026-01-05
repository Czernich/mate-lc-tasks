# Task: Write a function that rotates an array to the right by k steps.
# Example: [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3]

def rotate_array(nums: list, k: int) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=rotate_array([1, 2, 3, 4, 5], 2), expected_result=[4, 5, 1, 2, 3])
    validate_response(result=rotate_array([1, 2, 3, 4, 5], 0), expected_result=[1, 2, 3, 4, 5])
    validate_response(result=rotate_array([1, 2], 1), expected_result=[2, 1])
    validate_response(result=rotate_array([1, 2, 3], 4), expected_result=[3, 1, 2])
    validate_response(result=rotate_array([1], 5), expected_result=[1])
    validate_response(result=rotate_array([1, 2, 3, 4, 5, 6, 7], 3), expected_result=[5, 6, 7, 1, 2, 3, 4])

# Solution

def rotate_array(nums: list, k: int) -> list:
    if not nums:
        return nums
    
    n = len(nums)
    k = k % n
    
    return nums[-k:] + nums[:-k] if k > 0 else nums