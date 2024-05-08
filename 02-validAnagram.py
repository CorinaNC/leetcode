class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

# compare every character in s to every character in t
# create a list of characters for both and sort? if both are equal then true.