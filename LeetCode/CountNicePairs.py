class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            num = str(num)
            return int(num[::-1])
        
        d = dict()
        
        for num in nums:
            if num - rev(num) in d.keys():
                d[num-rev(num)] += 1
            else:
                d[num-rev(num)] = 1
        
        answer = 0
        
        for key, val in zip(d.keys(), d.values()):
            if val >= 2:
                answer += int(val*(val-1)//2)
        
        return answer % (10**9+7)