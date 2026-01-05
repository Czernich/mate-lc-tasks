# Task: Write a function that finds the intersection of two arrays.
# Return unique elements that appear in both arrays.
# The result can be in any order.

def intersection(nums1: list, nums2: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if sorted(result) == sorted(expected_result) else "FAIL")
    
    validate_response(result=intersection([1, 2, 2, 1], [2, 2]), expected_result=[2])
    validate_response(result=intersection([4, 9, 5], [9, 4, 9, 8, 4]), expected_result=[4, 9])
    validate_response(result=intersection([1, 2, 3], [4, 5, 6]), expected_result=[])
    validate_response(result=intersection([1], [1]), expected_result=[1])
    validate_response(result=intersection([1, 2, 3, 4], [3, 4, 5, 6]), expected_result=[3, 4])

# Solution

def intersection(nums1: list, nums2: list) -> list:
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)