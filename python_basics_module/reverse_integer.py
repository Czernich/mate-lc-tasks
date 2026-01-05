# Task: Write a function that reverses the digits of an integer.
# Preserve the sign (negative numbers stay negative).
# Example: 123 -> 321, -456 -> -654

def reverse_integer(n: int) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=reverse_integer(123), expected_result=321)
    validate_response(result=reverse_integer(-456), expected_result=-654)
    validate_response(result=reverse_integer(100), expected_result=1)
    validate_response(result=reverse_integer(0), expected_result=0)
    validate_response(result=reverse_integer(1), expected_result=1)
    validate_response(result=reverse_integer(-90), expected_result=-9)

# Solution

def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num