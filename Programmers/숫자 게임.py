def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    aIdx = 0
    
    for i in range(len(A)):
        if A[aIdx] < B[i]:
            answer += 1
            aIdx += 1
    
    return answer