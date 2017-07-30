class Solution(object):
    def leastInterval(self, tasks, n):
        task_map = {}
        for task in tasks:
            if task not in task_map:
                task_map[task] = 0
            task_map[task] += 1
        counts = task_map.items()
        counts.sort(key=lambda x : x[1], reverse=True)
        max_freq_count = 1
        for key, value in counts[1:]:
            if value == counts[0][1]:
                max_freq_count += 1
        return max(len(tasks), (counts[0][1] - 1) * (n + 1) + max_freq_count)


sol = Solution()
tasks = ['A','A','A','B','B','B']
assert sol.leastInterval(tasks, 2) == 8
tasks = ['A','A','A','B','B', 'C', 'C']
assert sol.leastInterval(tasks, 2) == 7


