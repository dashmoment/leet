"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ¡÷ false
isMatch("aa","aa") ¡÷ true
isMatch("aaa","aa") ¡÷ false
isMatch("aa", "*") ¡÷ true
isMatch("aa", "a*") ¡÷ true
isMatch("ab", "?*") ¡÷ true
isMatch("aab", "c*a*b") ¡÷ false

"""


class Solution:
# @return a boolean
    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        
        dp = [True] + [False]*length
        print(dp)
        for i in p:
            print(i)
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
                    print(dp, i, s[n])
                    
            else:
                
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
                    print(dp, i, s[n-1])
                    
            dp[0] = dp[0] and i == '*'
        return dp[-1]

s = Solution()
print(s.isMatch("abcde", "ab**e**e"))
