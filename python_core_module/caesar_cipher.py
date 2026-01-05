# Task: Write a function that encrypts a string using Caesar cipher with a given shift.
# Only shift alphabetic characters, preserve case, leave other characters unchanged.

def caesar_cipher(text: str, shift: int) -> str:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=caesar_cipher("abc", 3), expected_result="def")
    validate_response(result=caesar_cipher("xyz", 3), expected_result="abc")
    validate_response(result=caesar_cipher("Hello, World!", 5), expected_result="Mjqqt, Btwqi!")
    validate_response(result=caesar_cipher("ABC", 1), expected_result="BCD")
    validate_response(result=caesar_cipher("", 5), expected_result="")
    validate_response(result=caesar_cipher("Python 3.9", 13), expected_result="Clguba 3.9")

# Solution

def caesar_cipher(text: str, shift: int) -> str:
    result = []
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    
    return ''.join(result)