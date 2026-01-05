# Task: Write a function which checks if sequence of brackets is matching. 
# Function should take an integer with check range and return list of prime nubmers.



from typing import List

def primes_in_range(n: int) -> List[int]:
    # Write your code here
    pass


if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")

    validate_response(result=primes_in_range(1), expected_result=[])
    validate_response(result=primes_in_range(2), expected_result=[2])
    validate_response(result=primes_in_range(10), expected_result=[2,3,5,7])
    validate_response(result=primes_in_range(20), expected_result=[2,3,5,7,11,13,17,19])
    validate_response(result=primes_in_range(30), expected_result=[2,3,5,7,11,13,17,19,23,29])
    validate_response(result=primes_in_range(0), expected_result=[])
    validate_response(result=primes_in_range(3), expected_result=[2,3])
    validate_response(result=primes_in_range(5), expected_result=[2,3,5])
    validate_response(result=primes_in_range(50), expected_result=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
    validate_response(result=primes_in_range(100), expected_result=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])




# Solution

def primes_in_range(n: int) -> List[int]:
    primes = []

    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes