"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

"""
class Solution(object):
    def merge(self, intervals):
        """
        #:type intervals: List[Interval]
        #:rtype: List[Interval]

        """
        res = []
        sorted_intervals = sorted(intervals)
        stack = sorted_intervals[0]
        
        for idx in range(1, len(intervals)):

            if stack[1]-sorted_intervals[idx][0] >= 0:
                
                stack[0] = min(stack[0], sorted_intervals[idx][0])
                stack[1] = max(stack[1], sorted_intervals[idx][1])
                
            else:
                res.append([stack[0], stack[1]])
                stack[0] = sorted_intervals[idx][0]
                stack[1] = sorted_intervals[idx][1]
               
        if stack: res.append(stack)

        return res

"""
s = Solution()
print(s.merge([[1,3],[8,10],[2,6],[15,18]]))

