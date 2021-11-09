class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        for c in path.split("/"):
            if c == "..":
                if res:
                    res.pop()
            elif c == "." or not c:
                continue
            else:
                res.append(c)

        return "/" + "/".join(res)
