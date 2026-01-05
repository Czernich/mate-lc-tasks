# Task: Write a function that counts unique email addresses.
# Rules: 
# - Everything after '+' in local name is ignored
# - All '.' in local name are ignored
# - Domain name is case-sensitive
# Example: "test.email+alex@leetcode.com" -> "testemail@leetcode.com"

def num_unique_emails(emails: list) -> int:
    # Write your code here
    pass

if __name__ == "__main__":
    def validate_response(result, expected_result):
        print("OK" if result == expected_result else "FAIL")
    
    validate_response(
        result=num_unique_emails([
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ]),
        expected_result=2
    )
    validate_response(
        result=num_unique_emails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]),
        expected_result=3
    )
    validate_response(
        result=num_unique_emails(["test.email@leetcode.com", "test.email@leetcode.com"]),
        expected_result=1
    )
    validate_response(
        result=num_unique_emails(["test+1@leetcode.com", "test+2@leetcode.com"]),
        expected_result=1
    )

# Solution

def num_unique_emails(emails: list) -> int:
    unique = set()
    
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0]
        local = local.replace('.', '')
        unique.add(local + '@' + domain)
    
    return len(unique)