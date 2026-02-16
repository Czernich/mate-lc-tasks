# Task: Write a function which checks if sequence of brackets is matching. 
# Function should take a string with brackets and return True/False depending on check result.



def matching_brackets(s: str) -> bool:
    # Write your code here
    pass
        

if __name__ == "__main__":
    def validate_response(case, result, expected_result):
        result = "OK" if result is expected_result else "FAIL"
        print(f"{case:>2}: {result:>4}")
    
    validate_response(case=1,result=matching_brackets("[{()}]"), expected_result=True)
    validate_response(case=2,result=matching_brackets("[{(]"), expected_result=False)
    validate_response(case=3,result=matching_brackets("()"), expected_result=True)
    validate_response(case=4,result=matching_brackets("["), expected_result=False)
    validate_response(case=5,result=matching_brackets(""), expected_result=True)
    validate_response(case=6,result=matching_brackets("({[]})"), expected_result=True)
    validate_response(case=7,result=matching_brackets("({[})]"), expected_result=False)
    validate_response(case=8,result=matching_brackets("()[]{}"), expected_result=True)
    validate_response(case=9,result=matching_brackets("[{()()[]}]{}"), expected_result=True)
    validate_response(case=10,result=matching_brackets("((((()))))"), expected_result=True)
    validate_response(case=11,result=matching_brackets("(((()))"), expected_result=False)



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