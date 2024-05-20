class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(filter(str.isalnum, s))).lower()
        print(s)
        return s == s[::-1]

# basically just have to convert characters into
# lowercase, remove whitespace and non alphabeticals
# then compare original to reversed.