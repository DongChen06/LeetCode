class Solution:
    # bucket sort, O(N), O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        hashmap = collections.Counter(nums)
        for num, freq in hashmap.items():
            bucket[freq].append(num)
        bucket = list(chain(*bucket))
        return bucket[::-1][:k]