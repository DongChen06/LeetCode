# class Solution:
#     # O(N), O(N)
#     def findBuildings(self, heights: List[int]) -> List[int]:
#         res = []

#         for i in range(len(heights)):
#             while res and heights[res[-1]] <= heights[i]:
#                 res.pop()

#             res.append(i)

#         return res

class Solution:
    # O(N), O(1)
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]

        return res[::-1]