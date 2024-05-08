class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringMap = {}
        for word in strs:
            w = ''.join(sorted(word))
            if w not in stringMap:
                stringMap[w] = []
            stringMap[w].append(word)
        return stringMap.values()
# sort each word into characters
# conjoin character..
# apply each anagram to sorte dcharacter into map..
# return values