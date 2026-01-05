# Task: Write a function that checks if a given number is prime.
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n: int) -> bool:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result is expected_result else "FAIL")
    
    validate_response(result=is_prime(2), expected_result=True)
    validate_response(result=is_prime(1), expected_result=False)
    validate_response(result=is_prime(17), expected_result=True)
    validate_response(result=is_prime(20), expected_result=False)
    validate_response(result=is_prime(97), expected_result=True)
    validate_response(result=is_prime(100), expected_result=False)
    validate_response(result=is_prime(0), expected_result=False)
    validate_response(result=is_prime(-5), expected_result=False)

# Solution

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True