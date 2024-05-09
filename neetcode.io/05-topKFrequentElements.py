class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newDict = {}
        retList = []
        for num in nums:
            if num not in newDict:
                newDict[num] = 1
            else:
                newDict[num] += 1
        dictList = sorted(newDict.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            retList.append(dictList[i][0])
        return retList

# given 2, return the 2 more frequent elements in list [1, 1, 1, 2, 2, 3]
# topKFrequent([1, 1, 1, 2, 2, 3], 2)
# createa a dictionary for how many of each number there are in list?
# convert dictionary into iterable data structure
# then iterate through k range and append to list..

# then return the two highest keys...