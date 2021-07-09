class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n + 1):
            binary = bin(i)
            coun = binary.count("1")
            ans.append(coun)
        return ans


s = Solution()
print(s.countBits(8))
