# Task: Write a function that determines if a number is a power of two.
# A number is a power of two if it can be expressed as 2^n where n is a non-negative integer.

def is_power_of_two(n: int) -> bool:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result is expected_result else "FAIL")
    
    validate_response(result=is_power_of_two(1), expected_result=True)
    validate_response(result=is_power_of_two(16), expected_result=True)
    validate_response(result=is_power_of_two(3), expected_result=False)
    validate_response(result=is_power_of_two(0), expected_result=False)
    validate_response(result=is_power_of_two(8), expected_result=True)
    validate_response(result=is_power_of_two(218), expected_result=False)
    validate_response(result=is_power_of_two(-16), expected_result=False)

# Solution

def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0