# Task: Write a function that reverses the order of words in a sentence.
# Words are separated by spaces. Preserve single spaces between words.

def reverse_words(s: str) -> str:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=reverse_words("Hello World"), expected_result="World Hello")
    validate_response(result=reverse_words("Python is awesome"), expected_result="awesome is Python")
    validate_response(result=reverse_words("a"), expected_result="a")
    validate_response(result=reverse_words(""), expected_result="")
    validate_response(result=reverse_words("one two three four"), expected_result="four three two one")

# Solution

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])