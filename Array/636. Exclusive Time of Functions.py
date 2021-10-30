class Solution:
    # O(N), O(N)
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        pre_time = 0

        for log in logs:
            func, start, time = log.split(":")
            func, time = int(func), int(time)

            if start == "start":
                if stack:
                    res[stack[-1]] += time - pre_time
                pre_time = time
                stack.append(func)
            else:
                res[func] += time - pre_time + 1
                stack.pop()
                pre_time = time + 1

        return res