# Task: Write a function that finds all duplicate elements in a list.
# Return a list of unique duplicates (each duplicate should appear only once in result).

def find_duplicates(lst: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(case, result, expected_result):
        if result is not None:
            result_txt = "OK" if sorted(result) == sorted(expected_result) else "FAIL"
        else:
            result_txt = "FAIL"
        print(f"{case:>2}: {result_txt:>4}")
    
    validate_response(case=1,result=find_duplicates([1, 2, 3, 2, 4, 5, 1]), expected_result=[1, 2])
    validate_response(case=2,result=find_duplicates([1, 2, 3, 4, 5]), expected_result=[])
    validate_response(case=3,result=find_duplicates([]), expected_result=[])
    validate_response(case=4,result=find_duplicates([1, 1, 1, 1]), expected_result=[1])
    validate_response(case=5,result=find_duplicates([5, 5, 3, 3, 1, 1]), expected_result=[1, 3, 5])
    validate_response(case=6,result=find_duplicates([5, 5, 5, 3, 3, 1, 1]), expected_result=[1, 3, 5])
    validate_response(case=7,result=find_duplicates(["a", "b", "a", "c", "b"]), expected_result=["a", "b"])

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