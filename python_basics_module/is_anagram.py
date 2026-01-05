# Task: Write a function which checks if two strings are anagrams 
# (An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once).
# For example, "listen" and "silent" are anagrams.
# Function should take two strings and return True/False depending on check result.



def is_anagram(s1: str, s2: str) -> bool:
    # Write your code here
    pass


def validate_response(result, expected_result):
    print("OK" if result == expected_result else "FAIL")


if __name__ == "__main__":
    validate_response(result=is_anagram("listen", "silent"), expected_result=True)
    validate_response(result=is_anagram("triangle", "integral"), expected_result=True)
    validate_response(result=is_anagram("hello", "world"), expected_result=False)
    validate_response(result=is_anagram("Listen", "Silent"), expected_result=True)
    validate_response(result=is_anagram("abc", "ab"), expected_result=False)
    validate_response(result=is_anagram("a gentleman", "elegant man"), expected_result=True)
    validate_response(result=is_anagram("clint eastwood", "old west action"), expected_result=True)
    validate_response(result=is_anagram("", ""), expected_result=True)
    validate_response(result=is_anagram("a", "a"), expected_result=True)
    validate_response(result=is_anagram("a", "b"), expected_result=False)





# Solution

def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)
