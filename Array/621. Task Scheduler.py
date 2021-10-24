from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_val = max(freq.values())  # number of max_counting

        count = 0
        # ABC AB, count number of maximum encountering letters
        for num in sorted(freq.values(), reverse=True):
            if num == max_val:
                count += 1
            else:
                break

        idle = (max_val - 1) * n
        res = (max_val - 1) * (n + 1) + count

        # ABC ABC DEFG
        return max(len(tasks), res)