class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
    ''' for i in range(len(nums)):
            nums.remove(i)
            if i in nums:
                return True
        return False (thi ssolution does not work for all test cases)'''

# take first index: nums[0]
# compare nums[0] to nums[1]
# compare nums[0] to nums[2]
# compares nums[0] to nums[3]
# compare nums[0] to nums[4]

#... compare num[n] to num[n+1(+1(+1(+1)))]