class Solution(object):
    def longestCommonPrefix(self, strs):
      min_strs=min(len(s) for s in strs)

      st=""
      for i in range(min_strs):
        if all(s[i] == strs[0][i] for s in strs):
          st+=strs[0][i]
        else:
          break
      return st
a=Solution()
print(a.longestCommonPrefix(["shikhar","shivam","salini"]))