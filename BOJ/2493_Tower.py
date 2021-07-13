import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
stack = []
res = [0] * N

for idx, val in enumerate(tower):
    if idx == 0:
        stack.append([idx, val])
        continue
    else:
        while stack:
            if val < stack[-1][1]:
                res[idx] = stack[-1][0] + 1
                break
            else:
                stack.pop()
        stack.append([idx, val])

print(" ".join(map(str, res)))