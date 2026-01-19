# Task: Write a function that groups strings by their length.
# Return a dictionary where keys are lengths and values are lists of strings.

def group_by_length(words: list) -> dict:
    # Write your code here
    pass


if __name__ == "__main__":
    def validate_response(result, expected_result):
        if result is None:
            print("FAIL")
            return
        result_sorted = {k: sorted(v) for k, v in (result or {}).items()}
        expected_sorted = {k: sorted(v) for k, v in (expected_result or {}).items()}
        print("OK" if result_sorted == expected_sorted else "FAIL")
    
    validate_response(
        result=group_by_length(["a", "bb", "ccc", "dd", "e"]),
        expected_result={1: ["a", "e"], 2: ["bb", "dd"], 3: ["ccc"]}
    )
    validate_response(result=group_by_length([]), expected_result={})
    validate_response(result=group_by_length(["hello", "world"]), expected_result={5: ["hello", "world"]})
    validate_response(
        result=group_by_length(["one", "two", "three", "four"]),
        expected_result={3: ["one", "two"], 4: ["four"], 5: ["three"]}
    )


# Solution

def group_by_length(words: list) -> dict:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result