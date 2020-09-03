from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums_len = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            return False
        for idx,val in enumerate(nums):
            for j in range(idx+1,min(idx+1+k,nums_len)):
                if abs(val - nums[j]) <= t:
                    return True
        return False
        
