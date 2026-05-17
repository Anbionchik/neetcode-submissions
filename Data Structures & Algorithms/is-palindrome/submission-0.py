import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Z^a-z^0-9]', '', s).lower()
        return s == s[len(s)-1::-1]