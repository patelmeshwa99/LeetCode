import math
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l2=[]
        set_size=len(nums)
        for counter in range((int) (math.pow(2, set_size))):
            l1=[]
            for j in range(set_size):
                if((counter & (1 << j)) > 0): 
                    l1.append(nums[j])
            l2.append(l1)
            print("")
        return l2