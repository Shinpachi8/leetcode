class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        
        if nums[0] == nums[1]:
            return True
        
        dict_a = {}
        for i in nums:
            if i in dict_a:
                dict_a[i] += 1
            else:
                dict_a[i] = 1
        
        for i in dict_a:
            if dict_a[i] >= 2:
                index_temp = 0
                times = 0
                for index, value in enumerate(nums):
                    if value == i:
                        times += 1
                        if times == 1:
                            index_temp = index
                        if times == 2:
                            if index - index_temp <= k:
                                return True
                            else:
                                times = 1
                                index_temp = index
        return False