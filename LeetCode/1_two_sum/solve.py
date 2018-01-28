class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Original version (brute force)
        for idx, element in enumerate(nums):
            pair = target - element
            start = idx + 1
            if pair in nums[start:]:
                return [idx, nums[start:].index(pair) + start]


        ''' O(n) version
        pair = dict()
        for idx, element in enumerate(nums):
            if element in pair:
                return [pair[element], idx]
            else:
                pair[target - element] = idx
        '''
