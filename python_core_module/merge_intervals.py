# Task: Write a function that merges overlapping intervals.
# Each interval is represented as [start, end].
# Return the merged intervals sorted by start time.

def merge_intervals(intervals: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(result=merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]), expected_result=[[1, 6], [8, 10], [15, 18]])
    validate_response(result=merge_intervals([[1, 4], [4, 5]]), expected_result=[[1, 5]])
    validate_response(result=merge_intervals([[1, 4]]), expected_result=[[1, 4]])
    validate_response(result=merge_intervals([[1, 4], [0, 4]]), expected_result=[[0, 4]])
    validate_response(result=merge_intervals([[1, 4], [2, 3]]), expected_result=[[1, 4]])
    validate_response(result=merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]), expected_result=[[1, 6], [8, 12]])

# Solution

def merge_intervals(intervals: list) -> list:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:
            merged.append(current)
    
    return merged