class Solution(object):
    def makeBase(self, counts):
        base = []
        for i, x in enumerate(counts):
            if x > 0:
                for n in range(0, x/i):
                    a = [None]*i
                    base.append(a)
        return base
    
    def groupThePeople(self, groupSizes):
        counts = []
        for x in range(0,max(groupSizes)+1):
            counts.append(groupSizes.count(x))
        base = self.makeBase(counts)    
        
        for i, elem in enumerate(groupSizes):
            for arr in base:
                if len(arr) == elem and None in arr:
                    arr[arr.index(None)] = i
                    break
        return base
    

            
            
        