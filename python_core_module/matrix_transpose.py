# Task: Write a function that transposes a matrix (2D list).
# Transposing means converting rows to columns and columns to rows.

def transpose_matrix(matrix: list) -> list:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(
        result=transpose_matrix([[1, 2, 3], [4, 5, 6]]),
        expected_result=[[1, 4], [2, 5], [3, 6]]
    )
    validate_response(
        result=transpose_matrix([[1, 2], [3, 4], [5, 6]]),
        expected_result=[[1, 3, 5], [2, 4, 6]]
    )
    validate_response(
        result=transpose_matrix([[1]]),
        expected_result=[[1]]
    )
    validate_response(
        result=transpose_matrix([[1, 2, 3]]),
        expected_result=[[1], [2], [3]]
    )
    validate_response(
        result=transpose_matrix([[1], [2], [3]]),
        expected_result=[[1, 2, 3]]
    )

# Solution

def transpose_matrix(matrix: list) -> list:
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    
    return transposed