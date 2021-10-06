class Solution:
    def kClosest(self, points, k: int):
        distance = [(x[0] ** 2 + x[1] ** 2, x) for x in points]
        return [point for d, point in sorted(distance)[:k]]


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], k=2))
