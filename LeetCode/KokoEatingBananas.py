class Solution:
    def cannot_eat(piles, h, k):
        hours = 0
        for pile in piles:
            if pile % k == 0:
                hours += pile // k
            else:
                hours += pile // k + 1
        
        return hours > h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left+right)//2
            
            if Solution.cannot_eat(piles, h, mid):
                left = mid + 1
            else:
                right = mid
            
        return left