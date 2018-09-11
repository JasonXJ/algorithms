class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        n_not_visited = len(rooms)

        def dfs(i):
            nonlocal n_not_visited
            visited[i] = True
            n_not_visited -= 1
            if n_not_visited == 0:
                return True
            for j in rooms[i]:
                if not visited[j]:
                    if dfs(j):
                        return True
            return False

        return dfs(0)
