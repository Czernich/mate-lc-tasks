# Task: Write a function that calculates the sum of all digits in a number.
# For negative numbers, ignore the minus sign.

def sum_of_digits(n: int) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=sum_of_digits(123), expected_result=6)
    validate_response(result=sum_of_digits(0), expected_result=0)
    validate_response(result=sum_of_digits(999), expected_result=27)
    validate_response(result=sum_of_digits(-456), expected_result=15)
    validate_response(result=sum_of_digits(1), expected_result=1)
    validate_response(result=sum_of_digits(10203), expected_result=6)

# Solution

def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))