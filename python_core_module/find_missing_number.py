# Task: Write a function that finds the missing number in a sequence from 0 to n.
# Given a list containing n distinct numbers from range [0, n], find the missing number.

def find_missing_number(nums: list) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=find_missing_number([0, 1, 3]), expected_result=2)
    validate_response(result=find_missing_number([0, 1, 2, 3, 4, 6, 7]), expected_result=5)
    validate_response(result=find_missing_number([1, 2, 3, 4, 5]), expected_result=0)
    validate_response(result=find_missing_number([0]), expected_result=1)
    validate_response(result=find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 9]), expected_result=8)
    validate_response(result=find_missing_number([1]), expected_result=0)

# Solution

def find_missing_number(nums: list) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum