"""
Implement pow(x, n).
"""
"""
#Recursive Method

class Solution:
    def myPow(self, x, n):

        if n == 0: return 1

        if n < 0:
            n = -n
            x = 1.0/x
        
        if n%2 == 0:
            return self.myPow(x, n/2)*self.myPow(x, n/2)
        else:
            return self.myPow(x, n/2)*self.myPow(x, n/2)*x


"""

class Solution:
    def myPow(self, x, n):

        if n == 0: return 1
        if n < 0:
            n = -n
            x = 1.0/x

        res = x
        for i in range(2,n+1):
            res = res*x
        return res

s = Solution()
print(s.myPow(2, -3))
