class Solution:
    def partition(self, s: str):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if s == s[::-1]:
            path.append(s)
            res.append(path[:])
            path.pop()
        for i in range(1, len(s)):
            a = s[:i]
            if a == a[::-1]:
                path.append(a)
                self.dfs(s[i:], path, res)
                path.pop()


if __name__ == '__main__':
    s = "aab"
    sub_s = [["aa", "b"], ["a", "a", "b"]]
    res = Solution().partition(s)
    print(res)
