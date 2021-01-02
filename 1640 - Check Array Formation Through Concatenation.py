class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ans=[]
        for i in arr:
            for j in range(len(pieces)):
                if(i in pieces[j]):
                    ans.extend(pieces[j])
                    del pieces[j]
        if(ans==arr):
            return True
        else:
            return False