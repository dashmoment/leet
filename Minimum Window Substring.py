"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S."
"""

"""

class Solution(object):
    def minWindow(self, s, t):
       
        #:type s: str
        #:type t: str
        #:rtype: str
        

        window = len(t)
        stride = 1
        
        while window <= len(s):
            start = 0
            
            while start + window <= len(s):
                substr = s[start:start + window]
                test = list(s[start:start + window])
                match = 0
                for _t in t:
                    try:       
                        test.index(_t)
                        del test[test.index(_t)]
                        
                        match = match + 1
                        
                    except:
                        match = match
                if match == len(t): return substr 
                else:
                    start = start+stride
            window = window + 1
    
        return ""      
"""
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        print(collections.Counter(t))
        i = I = J = 0
        
        for j, c in enumerate(s, 1):
            print(j,c)
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                print(need, s[i],i,j)
                while i < j and need[s[i]] < 0:
                    
                    need[s[i]] += 1
                    print(need)
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
                print(I,J)
        return s[I:J]
s = Solution()
print(s.minWindow("ABBCABC","CBA"))

#print(s.minWindow("qxsncfwvbslazxuoxnedkukropehlwfbwxqycntdfgghecvdqbhcwtukkauwzzzvystcfohmupvastekunmqiidtjxriyqdyiyapohekxblrurbpgphoykjhjarhtwfduhvkpzumahdxagmivtxvgiepjvxetehnmczddurgdwdecrmzklxqubgfzfjslqizvheadvghrlnvcbxpnuhjxpqywzrkrbjokqpolxxflkapnzeatmltdbrackkwlvmwlbmxbjcmvebieilzwyszckzgulcihpgsssrtdvhaaligvvfrwaqyksegdjqmywfsoyotuxtwieefbjwxjpxvhcemnwzntgfjetdatyydecjgofdzudxbfbqsxpfsvmebijcbhcemfnuvtzupcrthujbuyiovvswdbagjdkxkyrftqbktvdcpogloqajlsgquiyfljcxjveengogbulsitexjeixwqpszoxkzzkiuooiweqxydqjywiiaqhyhwrgkosloetktjuponposfxrdhzdyibhesprjjczoyjhhgyxtnmlulextdatnecsyrlhangonsxxywutligguldpqgiemkymdjufycumwtjupfpdowjkjozzwjdivbvymrdlvzzstkmkpenfcyplnqkjzquutrsgiytdxsvsckftquzstqdihnrgfnbbevjovcutupnyburrpsjijmsqclyjzzk"
#, "fxtusxonrfdrhxjamdkwm"))


