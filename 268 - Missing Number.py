class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # This has time complexity of O(n) 
        idealList = [i for i in range(len(nums) + 1)]
        return set(idealList).difference(set(nums)).pop()

        # We could've also summed the numbers [0, len(nums)] and subtract it from sum(nums)
        # However, time complexity will remain same here
