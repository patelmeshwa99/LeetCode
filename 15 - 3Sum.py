from itertools import combinations 

class Solution:
    def threeSum(self, nums):
        also = []
        # nums = nums.sort()
        perm = combinations(nums, 3) 
        for i in perm:
            if(sum(i)==0):
                also.append(sorted(list(i)))
        unique_lst = []
        [unique_lst.append(sublst) for sublst in also if not unique_lst.count(sublst)]
        return sorted(unique_lst)
