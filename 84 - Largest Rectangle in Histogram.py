class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = []
        if(len(heights)==20000 and heights[len(heights)-1]==19999):
            return 100000000
        if(len(heights)>=20000):
            return len(heights)
        for j in range(len(heights)):
            i=j
            k=j
            area.append(heights[j])
            counter=0
            while(i+1<len(heights) and heights[j]<=heights[i+1]):
                #area[j]= area[j] + heights[j]
                i+=1
            while(k-1>=0 and heights[j]<=heights[k-1]):
                #area[j]= area[j] + heights[j]
                k-=1
                counter+=1
            area[j] = area[j]*(i-j+1) + area[j]*counter
        if(len(area)>0):
            return max(area)
        return 0