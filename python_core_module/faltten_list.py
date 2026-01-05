# Task: Write a function that flattens a nested list of arbitrary depth.
# Example: [1, [2, [3, 4], 5]] should become [1, 2, 3, 4, 5]

def flatten_list(lst: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=flatten_list([1, [2, 3], 4]), expected_result=[1, 2, 3, 4])
    validate_response(result=flatten_list([1, [2, [3, [4]]]]), expected_result=[1, 2, 3, 4])
    validate_response(result=flatten_list([]), expected_result=[])
    validate_response(result=flatten_list([1, 2, 3]), expected_result=[1, 2, 3])
    validate_response(result=flatten_list([[1], [2], [3]]), expected_result=[1, 2, 3])
    validate_response(result=flatten_list([1, [2, [3, 4], 5], 6]), expected_result=[1, 2, 3, 4, 5, 6])

# Solution

def flatten_list(lst: list) -> list:
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result