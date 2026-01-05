# Task: Write a function that returns the nth Fibonacci number.
# The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two.
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(n: int) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=fibonacci(0), expected_result=0)
    validate_response(result=fibonacci(1), expected_result=1)
    validate_response(result=fibonacci(2), expected_result=1)
    validate_response(result=fibonacci(5), expected_result=5)
    validate_response(result=fibonacci(10), expected_result=55)
    validate_response(result=fibonacci(15), expected_result=610)

# Solution

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b