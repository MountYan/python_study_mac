class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if not s or not wordDict:
            return False

        maxLen = 0
        wordDictSet = set()
        for e in wordDict:
            maxLen = max(maxLen, len(e))
            wordDictSet.add(e)

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i, -1, -1):
                if i - j > maxLen:
                    break
                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True

        return dp[-1]


if __name__ == '__main__':
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    flag = Solution().wordBreak(s, wordDict)
    print(flag)
