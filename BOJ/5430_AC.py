from sys import stdin
input = stdin.readline

def solution(cmds, nums, n):
    cmds.replace('RR', '') #뒤집기를 두 번 하면 뒤집지 않는 것과 같음
    s, e, rev = 0, 0, False
    for cmd in cmds:
        if cmd == 'R':
            rev = not rev
        elif cmd == 'D':
            if not rev: #역순정렬이 아닐 경우
                s += 1
            else:
                e += 1
        
    if s+e <= n:
        res = nums[s:n - e]
        if not rev:
            return '['+','.join(res)+']'
        else:
            return '['+','.join(res[::-1])+']'
    else:
        return 'error'

T = int(input())
for _ in range(T):
    cmds = input()
    n = int(input())
    nums = input().rstrip()[1:-1].split(',')
    if n==0: []
    ans = solution(cmds, nums, n)
    print(ans)
