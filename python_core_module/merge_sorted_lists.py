# Task: Write a function that merges two sorted lists into one sorted list.
# CAUTION: You cannot use sort() and sorted() functions

def merge_sorted_lists(list1: list, list2: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=merge_sorted_lists([1, 3, 5], [2, 4, 6]), expected_result=[1, 2, 3, 4, 5, 6])
    validate_response(result=merge_sorted_lists([], [1, 2, 3]), expected_result=[1, 2, 3])
    validate_response(result=merge_sorted_lists([1, 2, 3], []), expected_result=[1, 2, 3])
    validate_response(result=merge_sorted_lists([1], [2]), expected_result=[1, 2])
    validate_response(result=merge_sorted_lists([3], [1]), expected_result=[1, 3])
    validate_response(result=merge_sorted_lists([1, 5, 9], [2, 3, 7, 10]), expected_result=[1, 2, 3, 5, 7, 9, 10])

# Solution

def merge_sorted_lists(list1: list, list2: list) -> list:
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result