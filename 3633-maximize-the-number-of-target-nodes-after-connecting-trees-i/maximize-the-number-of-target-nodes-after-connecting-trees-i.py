class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def bfs(mp: dict, start: int, max_depth: int) -> int:
            visited = [False] * (max(mp.keys()) + 1)
            q = deque([(start, 0)])
            count = 0
            while q:
                node, depth = q.popleft()
                if visited[node] or depth > max_depth:
                    continue
                visited[node] = True
                count += 1
                for nei in mp[node]:
                    if not visited[nei]:
                        q.append((nei, depth + 1))
            return count
        
        def build_graph(edges: List[List[int]]) -> defaultdict:
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        mp1 = build_graph(edges1)
        mp2 = build_graph(edges2)

        n, m = len(edges1) + 1, len(edges2) + 1
        cal1 = [bfs(mp1, i, k) for i in range(n)]
        max_cal2 = max(bfs(mp2, i, k - 1) for i in range(m))

        return [cal1[i] + max_cal2 for i in range(n)]