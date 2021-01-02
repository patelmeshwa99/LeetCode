class Solution:
    def nearestGreaterLeft(self,arr,n):
        res=[];
        for i in range(n):
            total=1;
            temp = i-1;
            while temp >= 0 and arr[i] <= arr[temp]:
                total+=1;
                temp-=1;
        
            res.append(total)
        return res
    
    def nearestGreaterRight(self,arr,n):
        res=[];
        for i in range(n):
            temp = i+1;
            total=0;
            while temp < n and arr[temp] >= arr[i]:
                total+=1;
                temp+=1;
            res.append(total)
        return res
                
               
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        elif n==1:
            return heights[0]
        
        equal = True
        for i in range(n-1):
            if heights[i]!=heights[i+1]:
                equal=False
                break;
        if equal:
            return heights[0]*n
        if n > 2:
            sorted=True;
            for i in range(n-1):
                if heights[i] >= heights[i+1]:
                    sorted = False;
                    break;
            if sorted:
                mid = int(n/2);
                return (n-mid) * heights[mid];

        left = self.nearestGreaterLeft(heights,n)
        right = self.nearestGreaterRight(heights,n)
        max=0;
        for i in range(len(left)):
            temp = ((right[i] + left[i])) * heights[i];
            if max < temp:
                max=temp;
        return max;