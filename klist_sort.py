
def min_(lists):

    minval = lists[0]

    for i in range(1, len(lists)):
        if lists[i] != None:
            if lists[i] <  minval: minval = lists[i]
            else: minval = minval
    if minval == None:
        return "None"
    else: return minval

class listnode:
    def __init__(self, value, link=None):
        self.value = value
        self.link  = link


class solution:
    def mergesort(self, lists):

        current_idx = []
        print(lists[0])
        [current_idx.append(len(lists[i])) for i in range(len(lists))]

        results = listnode(0)
        head = results
        comp = []

        while True:
            for idx in range(len(current_idx)):
                
                if current_idx[idx] <= 0 or len(lists[idx]) == 0: comp.append(None)
                else: comp.append(lists[idx].value)

                minval = min_(comp)
                if minval == "None": return results
                else:
                    move_idx = comp.index(minval)
                    current_idx[move_idx] -= 1 
                    head.link = listnode(minval)
                    head = head.link


s = solution()
print(s.mergesort([[]]))
                
