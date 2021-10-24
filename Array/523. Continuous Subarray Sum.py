class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        reminders = {0: -1}

        curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            reminder = curr_sum % k

            if reminder in reminders and idx - reminders[reminder] > 1:
                return True
            if reminder not in reminders:
                reminders[reminder] = idx