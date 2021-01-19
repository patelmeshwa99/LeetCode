class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=1
        length=len(s)
        start=0
        low=0
        high=0
        for i in range(1,length):
            #Longest palindrome with even length
            low=i-1
            high=i
            while low>=0 and high<length and s[low]==s[high]:
                if high-low+1>maxlen:
                    start = low
                    maxlen = high-low+1
                low-=1
                high+=1
            
            #Longest plaindrome with odd length
            low=i-1
            high=i+1
            while low>=0 and high<length and s[low]==s[high]:
                if high-low+1>maxlen:
                    start = low
                    maxlen = high-low+1
                low-=1
                high+=1
        return s[start:start+maxlen]
        