from itertools import permutations
import re

def solution(expression):
    operator = ['*', '+', '-']
    priority = list(permutations(operator, 3)) #모든 경우의 수
    result = []

    for pri in priority:
        # 정규 표현식을 사용하여 숫자와 연산자 분리
        nums = re.findall('\d+', expression)
        ops = re.findall('[*+-]', expression)
        res = 0
        before = ''
        
        for p in pri:
            remove_cnt = 0 #연산자를 삭제한 횟수
            for idx, op in enumerate(ops):
                if op == p:
                    res = eval(str(nums[idx-remove_cnt]) + op + str(nums[idx-remove_cnt + 1])) 
                    nums[idx-remove_cnt] = int(res) #현재 연산자의 index에 삭제 횟수를 빼준 값을 index로 함
                    del nums[idx-remove_cnt+1]
                    ops[idx] = '0'
                    remove_cnt += 1
                    
            ops = [i for i in ops if i != '0']

        result.append(abs(res))

    answer = max(result)
    return answer