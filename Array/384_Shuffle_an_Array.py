import random


class Solution:

    def __init__(self, nums):
        self.ori = nums
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.ori
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
