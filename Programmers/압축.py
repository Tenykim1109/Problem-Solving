def solution(msg):
    answer = []
    alphaDict = {}
    
    for i in range(26):
        alphaDict[chr(65+i)] = i+1
    
    w, c = 0, 0  
    while True:
        c += 1
        if c == len(msg):
            answer.append(alphaDict[msg[w:c]])
            break
        
        if msg[w:c+1] not in alphaDict:
            alphaDict[msg[w:c+1]] = len(alphaDict) + 1
            answer.append(alphaDict[msg[w:c]])
            w = c
            
    return answer

print(solution('KAKAO'))
print(solution('A'))