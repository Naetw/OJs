class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict

        remain_set = set(range(1, N + 1))
        time = [float('inf')] * (N + 1)
        nodes = defaultdict(dict)
        for u, v, w in times:
            nodes[u][v] = w

        time[K] = 0
        while len(remain_set):

            # pick node with minimum time
            pick = 0
            for i in remain_set:
                if time[i] <= time[pick]:
                    pick = i
            remain_set.remove(pick)

            # update adjacent nodes
            for key in nodes[pick].keys():
                tmp = time[pick] + nodes[pick][key]
                if time[key] > tmp:
                    time[key] = tmp

        ret = max(time[1:])
        return -1 if ret == float('inf') else ret
