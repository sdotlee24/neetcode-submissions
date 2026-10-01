class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum() or not s[r].isalnum():
                print(f"not alnum: {s[l]} and {s[r]}")
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
            else:
                print(f"{s[l]} and {s[r]}")
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            

        return True
            