class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            foun = [j for j in range(nums.index(i)+1,len(nums)) if i + nums[j] == target]
            if len(foun) > 0 and i + nums[foun[0]] == target:
                return [nums.index(i), foun[0]]
