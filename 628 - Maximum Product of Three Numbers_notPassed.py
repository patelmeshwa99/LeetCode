import math
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        flag=True
        x=set(nums)
        count=0

        while(flag):
            item = x.pop()
            if(item==k/2):
                count+=math.floor(nums.count(item)/2)
            else:
                if(nums.count(k-item)!=0):
                    count+=min(nums.count(item),nums.count(k-item))
                    # inter = list(x)
                    # inter.remove(k-item)
                    x=set(filter(lambda x:x!=k-item, x))
            if(len(x)==0):
                flag=False
        return count
            