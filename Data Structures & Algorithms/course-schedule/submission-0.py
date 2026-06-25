class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses


        adj = defaultdict(list)

        indegree = [0] * n

        # we need to build the adj graph
        for a,b in prerequisites:
            # need to take b to get a so a depends on it
            # edge from b -> a
            adj[b].append(a)
            indegree[a] += 1

        # add all values with indegree 0 onto the queue
        queue = collections.deque([i for i in range(n) if indegree[i] == 0])

        res = 0

        # then we should go through and then process the classes

        while queue:
            # we need to remove the i class
            pre_req = queue.popleft()
            res += 1
            # we need to remove this from all values that depend on it
            for dependency in adj[pre_req]:
                indegree[dependency] -= 1
                if indegree[dependency] == 0:
                    queue.append(dependency)

        return res == n

