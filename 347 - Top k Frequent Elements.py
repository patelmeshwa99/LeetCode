class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = dict((i, nums.count(i)) for i in set(nums))
        ans = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
        return list(ans.keys())[0:k]
        