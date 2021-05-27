class Solution:
    def brokenCalc(self, x: int, y: int) -> int:   
        cnt = 0
        
        while y>x:
            cnt+=1
            
            if y%2==0:
                y //= 2
            else:
                y += 1
        
        return cnt + x-y