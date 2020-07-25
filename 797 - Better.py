class Solution(object):
    def allPathsSourceTarget(self, graph):
        ans=[]
        n=len(graph)
        path=[]
        visited=[False]*n
        def findpaths(vertex):
            nonlocal n
            visited[vertex]=True
            path.append(vertex)
            if vertex==n-1:
                ans.append(path[:])
            else:
                for neig in graph[vertex]:
                    if not visited[neig]:
                        findpaths(neig)
            visited[vertex]=False
            path.pop()
        findpaths(0)
        return ans