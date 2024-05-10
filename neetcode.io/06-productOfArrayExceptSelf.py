class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        ls = [1] * len(nums)
        bef = [1] * len(nums)
        aft = [1] * len(nums)
        for i in range(1, len(nums)):
            bef[i] = bef[i-1] * nums[i-1]
        print(bef)
        for i in range(len(nums)-2, -1, -1):
            aft[i] = aft[i+1] * nums[i+1]
        print(aft)
        for i in range(len(nums)):
            ls[i] = bef[i]*aft[i]
        return ls
'''        retList = []
        for i in range(len(nums)):
            prod = 1
            mulList = nums.copy()
            del mulList[i]
            for num in mulList:
                prod *= num
            retList.append(prod)
        return retList (original solution, too slow.)'''

# prodExceptSelf([1, 2, 3, 4]):
# ls = [1, 1, 1, 1]
# bef = [1, 1, 1, 1]
# aft = [1, 1, 1, 1]
# for i in range(1, 4)
# bef[1] = bef[0] * nums[0] -> bef[0] = 1 * 1  -> 1
# bef[2] -> 1 * 2 -> 2
# bef[3] = bef[3-1] * nums[3-1] -> bef[2] * nums[2] -> 2 * 3 -> 6
# aft[2] = aft[3] * nums[3] -> 1 * 4 -> 4
# after[1] = after[2] * nums[2] -> 3 * 4 -> 12
# aft[0] = after[1] * nums[1] -> 12 * 1 -> 1
# now bef = [1, 1, 2, 6]
# now aft = [24, 12, 4, 1]
# for i in range(len(nums)):
# ls[0] = bef[0] * aft[0] -> 24... and so on.
# ls is now [1, 1, 2, 6] * [24, 12, 4, 1] -> [24, 12, 8, 6]
