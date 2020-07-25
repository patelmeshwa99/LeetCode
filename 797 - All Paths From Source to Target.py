class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        x=[]
        a=[]
        for i in range(len(graph)-1):
            for j in range(len(graph[i])):
                if(i==0):
                    x.append([i,graph[i][j]])
                else:
                    x = self.check(x,i,graph[i])
                    break
        
        for i in range(len(x)):
            if(x[i][len(x[i])-1]==graph[len(graph)-2][-1]):
                a.append(x[i])
        return a
                
                    
    def check(self, x, index, val):
        i=0
        while(i<len(x)):
            if(x[i][len(x[i])-1]==index):
                inc = i
                if(len(val)==1):
                    x[i].append(val[0])
                else:
                    for m in range(len(val)):
                        ans=x[inc].copy()
                        ans.append(val[m])
                        x.insert(inc,ans)
                        inc+=1
                    del x[inc]
            i+=1
        return x