from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegree[cur] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        order = []

        while queue:
            pre = queue.pop(0)
            order.append(pre)

            for i in adjacency[pre]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(order) == numCourses:
            return order
        else:
            return []
