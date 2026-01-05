# Task: Write a function that returns an array where each element is the product 
# of all elements in the input array except the element at that index.
# Do not use division operation.

def product_except_self(nums: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=product_except_self([1, 2, 3, 4]), expected_result=[24, 12, 8, 6])
    validate_response(result=product_except_self([2, 3, 4, 5]), expected_result=[60, 40, 30, 24])
    validate_response(result=product_except_self([1, 1, 1, 1]), expected_result=[1, 1, 1, 1])
    validate_response(result=product_except_self([5]), expected_result=[1])
    validate_response(result=product_except_self([1, 2]), expected_result=[2, 1])
    validate_response(result=product_except_self([0, 1, 2]), expected_result=[2, 0, 0])

# Solution

def product_except_self(nums: list) -> list:
    n = len(nums)
    result = [1] * n
    
    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # Right products
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result