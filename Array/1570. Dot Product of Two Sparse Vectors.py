class SparseVector:
    # O(n), O(L)
    def __init__(self, nums: List[int]):
        self.nozeros = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nozeros[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, n in self.nozeros.items():
            if i in vec.nozeros:
                res += n * vec.nozeros[i]

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)