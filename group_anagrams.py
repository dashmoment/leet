"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class solution:
    def group_anagrams(self, lists):

        res = {}

        for s in lists:
            key = tuple(sorted(s))

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return res

s = solution()
print(s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        
