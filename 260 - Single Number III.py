class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = dict()
        ans = []
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if(v==1):
                ans.append(k)
        return ans