# Task: Write a function that calculates the factorial of a non-negative integer.
# Factorial of n (n!) is the product of all positive integers less than or equal to n.
# By definition, 0! = 1.

def factorial(n: int) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=factorial(0), expected_result=1)
    validate_response(result=factorial(1), expected_result=1)
    validate_response(result=factorial(5), expected_result=120)
    validate_response(result=factorial(3), expected_result=6)
    validate_response(result=factorial(10), expected_result=3628800)
    validate_response(result=factorial(7), expected_result=5040)

# Solution

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result