class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        new_intervals = []

        for interval in intervals:
            if new_intervals == [] or new_intervals[-1][1] < interval[0]:
                new_intervals.append(interval)
            else:
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])

        return new_intervals