class Solution:
    # O(nlogn), O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return None
        nums.sort()
        return nums[-k]


class Solution:
    # O(k + ) time, O(k); min-heap
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapify(heap)
        for n in nums[k:]:
            heappushpop(heap, n)
        return heap[0]


class Solution:
    # O(k + ) time, O(k), quick search
    def findKthLargest(self, nums, k):
        # p = nums[0]
        p = random.choice(nums)
        left = [n for n in nums if n > p]
        mid = [n for n in nums if n == p]
        right = [n for n in nums if n < p]

        if k <= len(left):  ## <=
            return self.findKthLargest(left, k)
        elif k > len(left) + len(mid):
            return self.findKthLargest(right, k - len(left) - len(mid))  ## k - l - m
        else:
            return mid[0]