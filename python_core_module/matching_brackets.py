# Task: Write a function which checks if sequence of brackets is matching. 
# Function should take a string with brackets and return True/False depending on check result.



def matching_brackets(s: str) -> bool:
    # Write your code here
    pass
        

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result is expected_result else "FAIL")
    
    validate_response(result=matching_brackets("[{()}]"), expected_result=True)
    validate_response(result=matching_brackets("[{(]"), expected_result=False)
    validate_response(result=matching_brackets("()"), expected_result=True)
    validate_response(result=matching_brackets("["), expected_result=False)
    validate_response(result=matching_brackets(""), expected_result=True)
    validate_response(result=matching_brackets("({[]})"), expected_result=True)
    validate_response(result=matching_brackets("({[})]"), expected_result=False)
    validate_response(result=matching_brackets("()[]{}"), expected_result=True)
    validate_response(result=matching_brackets("[{()()[]}]{}"), expected_result=True)
    validate_response(result=matching_brackets("((((()))))"), expected_result=True)
    validate_response(result=matching_brackets("(((()))"), expected_result=False)



# Solution

def matching_brackets(s: str) -> bool:
    stack = []
    bracket_pairs = {"[": "]", "{": "}", "(": ")"}

    for bracket in s:
        if bracket in bracket_pairs:
            stack.append(bracket)
        else:
            if bracket_pairs[stack[-1]] == bracket:
                stack.pop()
            else:
                return False

    return not stack