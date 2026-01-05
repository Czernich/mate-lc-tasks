# Task: Write a function that converts an Excel column title to its corresponding column number.
# A -> 1, B -> 2, ... Z -> 26, AA -> 27, AB -> 28, etc.
# 
# Hint: You can use ord() function to get ASCII value of a character.
# ord('A') returns 65, ord('B') returns 66, etc.
# To get position: ord(char) - ord('A') + 1
# Example: ord('C') - ord('A') + 1 = 67 - 65 + 1 = 3

def title_to_number(s: str) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=title_to_number("A"), expected_result=1)
    validate_response(result=title_to_number("AB"), expected_result=28)
    validate_response(result=title_to_number("ZY"), expected_result=701)
    validate_response(result=title_to_number("Z"), expected_result=26)
    validate_response(result=title_to_number("AA"), expected_result=27)
    validate_response(result=title_to_number("AZ"), expected_result=52)

# Solution

def title_to_number(s: str) -> int:
    result = 0
    
    for char in s:
        result = result * 26 + (ord(char) - ord('A') + 1)
    
    return result