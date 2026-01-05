# Task: Write a function that finds all duplicate elements in a list.
# Return a list of unique duplicates (each duplicate should appear only once in result).

def find_duplicates(lst: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if sorted(result) == sorted(expected_result) else "FAIL")
    
    validate_response(result=find_duplicates([1, 2, 3, 2, 4, 5, 1]), expected_result=[1, 2])
    validate_response(result=find_duplicates([1, 2, 3, 4, 5]), expected_result=[])
    validate_response(result=find_duplicates([]), expected_result=[])
    validate_response(result=find_duplicates([1, 1, 1, 1]), expected_result=[1])
    validate_response(result=find_duplicates([5, 5, 3, 3, 1, 1]), expected_result=[1, 3, 5])
    validate_response(result=find_duplicates(["a", "b", "a", "c", "b"]), expected_result=["a", "b"])

# Solution

def find_duplicates(lst: list) -> list:
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)