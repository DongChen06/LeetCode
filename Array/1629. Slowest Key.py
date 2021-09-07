class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = releaseTimes[0]
        char = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > longest:
                longest = duration
                char = keysPressed[i]
            elif duration == longest:
                if keysPressed[i] > char:
                    char = keysPressed[i]

        return char