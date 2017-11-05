"""
218. The Skyline Problem
"""

class Solution(object):


	def getSkyline(self,buildings):


	    skylines = []
	    for b in buildings:
	        skylines.append([[b[0], b[2]],[b[1], 0]])

	    idx = 0
	    results = []
	    for i in range(len(skylines)):

	    	print([results, skylines[i]])
	    	results =  self.mergeSkylines([results, skylines[i]])
	    	print("tmp", results)


			
	    return results


	def mergeSkylines(self, skylines):
	    
	    num = len(skylines)
	   
	    
	    if num == 1: return skylines[0]
	    
	    if num == 2:
	    	l_skyline = skylines[0]
	    	r_skyline = skylines[1]
		       
		yl = 0
		yr = 0
		x = 0
		full_skyline = []

		while len(l_skyline) > 0 or len(r_skyline) > 0:
		            
		    if len(l_skyline) == 0:
		        full_skyline.extend(r_skyline)
		        break
		        
		    if len(r_skyline) == 0:
		        full_skyline.extend(l_skyline)
		        break
		        
		    xl = l_skyline[0]
		    xr = r_skyline[0]


		    
		    if xl[0] < xr[0]:
		    
		        p = l_skyline.pop(0)
		        x = p[0]
		        yl = p[1]
		        
		    else:
		        p = r_skyline.pop(0)
		        x = p[0]
		        yr = p[1]

		    
		        
		    full_skyline.append([x,max(yl,yr)])
		print("full_skyline", full_skyline)

		fixed_full_skyline = [full_skyline[0]] 
		
		
		for p in full_skyline:
			if p[1] != fixed_full_skyline[-1][1]:
				
				
				if p[0] == fixed_full_skyline[-1][0]:

					if p[0] == full_skyline[-1][0]:
						fixed_full_skyline[-1][1] = min(p[1], fixed_full_skyline[-1][1])
					else:
						fixed_full_skyline[-1][1] = max(p[1], fixed_full_skyline[-1][1])
				else:
					fixed_full_skyline.append(p)
				
				#fixed_full_skyline.append(p)

		return fixed_full_skyline
	        
		

test_buildings = [[2,6,3], [4,5,6]]
buildings = test_buildings
events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
print(events)
res, hp = [[0, 0]], [(0, float("inf"))]
import heapq

for x, negH, R in events:
        while x >= hp[0][1]: 
            heapq.heappop(hp)
        
        if negH: 
            heapq.heappush(hp, (negH, R))
        print("heap", [x, negH, R],hp)
        print(res[-1][1], hp[0][0], bool(res[-1][1] +  hp[0][0]))
        if res[-1][1] + hp[0][0]: 
            res += [x, -hp[0][0]],
        print("res: ", res)

a = 10 

print(False or True and True)
"""
s = Solution()
test_ = s.getSkyline(test_buildings)
print(test_)
"""