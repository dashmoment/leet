"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = False
        if not s: return True
        
        for i in range(len(wordDict)):

            if wordDict[i] in s:
                print(s, wordDict[i])
                s_copy = s.split(wordDict[i])
                print(s_copy, wordDict[i])

                res = True
                for j in range(len(s_copy)):
                    res =  res and self.wordBreak(s_copy[j], wordDict)
                    if res == False: break
            if res==True: return True
            

        return False

s = Solution()
print(s.wordBreak("ccbb", ["bc", "cb"]))
