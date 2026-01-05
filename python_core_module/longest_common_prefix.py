# Task: Write a function that finds the longest common prefix among an array of strings.
# If there is no common prefix, return an empty string.

def longest_common_prefix(strs: list) -> str:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=longest_common_prefix(["flower", "flow", "flight"]), expected_result="fl")
    validate_response(result=longest_common_prefix(["dog", "racecar", "car"]), expected_result="")
    validate_response(result=longest_common_prefix(["interspecies", "interstellar", "interstate"]), expected_result="inters")
    validate_response(result=longest_common_prefix(["a"]), expected_result="a")
    validate_response(result=longest_common_prefix([]), expected_result="")
    validate_response(result=longest_common_prefix(["abc", "abc", "abc"]), expected_result="abc")

# Solution

def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix