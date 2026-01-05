# Task: Write a function that checks if string s is a subsequence of string t.
# A subsequence is formed by deleting some (or no) characters without changing the order.
# Example: "ace" is a subsequence of "abcde"

def is_subsequence(s: str, t: str) -> bool:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result is expected_result else "FAIL")
    
    validate_response(result=is_subsequence("ace", "abcde"), expected_result=True)
    validate_response(result=is_subsequence("aec", "abcde"), expected_result=False)
    validate_response(result=is_subsequence("", "abcde"), expected_result=True)
    validate_response(result=is_subsequence("abc", "abc"), expected_result=True)
    validate_response(result=is_subsequence("abc", "ab"), expected_result=False)
    validate_response(result=is_subsequence("axc", "ahbgdc"), expected_result=False)

# Solution

def is_subsequence(s: str, t: str) -> bool:
    s_idx = 0
    
    for char in t:
        if s_idx < len(s) and char == s[s_idx]:
            s_idx += 1
    
    return s_idx == len(s)