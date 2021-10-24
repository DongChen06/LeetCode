class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for index, le in enumerate(order):
            hashmap[le] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # case: apple app
                if j >= len(words[i + 1]):
                    return False

                if hashmap[words[i][j]] != hashmap[words[i + 1][j]]:
                    # case: unsorted
                    if hashmap[words[i][j]] > hashmap[words[i + 1][j]]:
                        return False
                    # if we find the first unsorted pair, then break
                    break

        return True