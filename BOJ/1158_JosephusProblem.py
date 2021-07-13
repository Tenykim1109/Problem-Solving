import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = [i for i in range(1, n+1)]
res = []

idx = k - 1
while queue:
    if idx >= len(queue):
        idx = idx%len(queue)

    res.append(queue[idx])
    del queue[idx]

    idx += k - 1


print("<", end="")
print(", ".join(map(str, res)), end="")
print(">")