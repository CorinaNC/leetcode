class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapToIndex = {}
        for i in range(len(nums)):
            if target-nums[i] in mapToIndex:
                return sorted([i, mapToIndex[target-nums[i]]])
            mapToIndex[nums[i]] = i
''' (my original solution which was simpy too slow.)  iList = []
        otherNums = nums.copy()
        for i in range(len(nums)):
            otherNums = nums.copy()
            currentNum = otherNums[i]
            otherNums[i] = 'current'
            for j in range(len(nums)):
                if target-currentNum in otherNums:
                    iList.append(i), iList.append(otherNums.index(target-currentNum))
                    return iList '''
# input [2, 7, 11, 15]
# target = 9
# return indices of 2 + 7, so input[0] input[1], so [0, 1]
# we want to save the indexes so range(len(nums)) for sure...
# could also gather the index directly...
# maybe subtraction? trying to get index to skip itself though..
'''
# [2, 7, 11, 15]
# twoSum([2, 7, 11, 15], 9)
# numToIndex = {}
# for i in range(4):
    if 7 in {}:
        return [numToIndex[7], 0]
    numToIndex[2] = 0
'''