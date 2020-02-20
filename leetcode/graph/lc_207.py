#coding: utf-8
import sys
from typing import List

sys.setrecursionlimit(99999)


class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """通过邻接表保存图，每次去掉入度为0的顶点

        Arguments:
            numCourses {int} -- [description]
            prerequisites {List[List[int]]} -- [description]

        Returns:
            bool -- [description]
        """
        graph = {}
        for i in range(numCourses):
            graph[i] = 0
        for pre in prerequisites:
            graph[pre[0]] = graph[i] + 1
        while True:
            removed = False
            for i in range(numCourses):
                exist = i in graph and graph[i]
                if not exist:
                    for _, v in graph.items():
                        if i in v:
                            v.remove(i)
                            removed = True
            if not removed:
                break
        return all(not v for v in graph.values())

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = {}
        for pre in prerequisites:
            graph[pre[0]][pre[1]] = 1
        while True:
            removed = False
            for i in range(numCourses):
                exist = len(graph[i]) > 0
                if not exist:
                    for v in graph.values():
                        if i in v:
                            v.pop(i)
                            removed = True
            if not removed:
                break
        return all(not v for v in graph.values())

    def canFinishBfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """拓扑排序解法

        Arguments:
            numCourses {int} -- [description]
            prerequisites {List[List[int]]} -- [description]

        Returns:
            bool -- [description]
        """
        indegree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        # 没有被其他课程依赖的节点
        queue = []
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    queue.append(cur)

        return numCourses == 0

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adjacency, i, visited):
            """深度遍历

            Arguments:
                self {[type]} -- [description]
                i {[type]} -- [description]
                visited {[type]} -- [description]

            Returns:
                bool -- 有环: False  无环: True
            """
            # 如果被其他dfs访问，则返回True，不重复访问
            if visited[i] == -1:
                return True
            # 如果被dfs访问过，则说明有环
            if visited[i] == 1:
                return False
            visited[i] = 1
            for v in adjacency[i]:
                if not dfs(adjacency, v, visited):
                    return False

            visited[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        # 记录该顶点的访问记录
        # 0：未被访问
        # 1：已被当前dfs访问
        # -1：被其他dfs访问
        visited = [0] * numCourses
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if not dfs(adjacency, i, visited):
                return False
        return True
