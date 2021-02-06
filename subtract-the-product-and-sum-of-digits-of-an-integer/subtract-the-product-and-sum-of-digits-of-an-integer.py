class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0
        product = 1
        for x in str(n):
            sum += int(x)
            product *= int(x)
        return product - sum
        
        