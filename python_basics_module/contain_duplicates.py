# Task: Write a function that checks if an array contains any duplicate values.
# Return True if any value appears at least twice, False otherwise.

def contains_duplicate(nums: list) -> bool:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result is expected_result else "FAIL")
    
    validate_response(result=contains_duplicate([1, 2, 3, 1]), expected_result=True)
    validate_response(result=contains_duplicate([1, 2, 3, 4]), expected_result=False)
    validate_response(result=contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), expected_result=True)
    validate_response(result=contains_duplicate([]), expected_result=False)
    validate_response(result=contains_duplicate([1]), expected_result=False)
    validate_response(result=contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]), expected_result=True)

# Solution

def contains_duplicate(nums: list) -> bool:
    return len(nums) != len(set(nums))