# Task: Write a function that returns a list of strings from 1 to n where:
# - For multiples of 3, append "Fizz"
# - For multiples of 5, append "Buzz"
# - For multiples of both 3 and 5, append "FizzBuzz"
# - Otherwise, append the number as a string

def fizzbuzz(n: int) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(
        result=fizzbuzz(15),
        expected_result=["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    )
    validate_response(result=fizzbuzz(5), expected_result=["1", "2", "Fizz", "4", "Buzz"])
    validate_response(result=fizzbuzz(1), expected_result=["1"])
    validate_response(result=fizzbuzz(3), expected_result=["1", "2", "Fizz"])

# Solution

def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result