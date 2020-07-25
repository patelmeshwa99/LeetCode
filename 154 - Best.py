class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums)-1
        
        while lo < hi:
            mid = (lo+hi)//2
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[hi] >= nums[mid]:
                hi = mid
            else:
                lo = mid+1
        return nums[lo]