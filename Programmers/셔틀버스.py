from collections import deque
from datetime import timedelta

def solution(n, t, m, timetable):
    answer = ''
    timeint = [int(x[0])*60 + int(x[1]) for x in list(map(lambda x : x.split(":"), timetable))]
    timeint.sort()
    timeint = deque(timeint)
    last_time = 60*9 + t*(n-1);
    capacity = m*n
    answerint = -1

    for i in range(n) :
        tmpcap = 0
        for j in range(m) :
            if len(timeint) == 0 :
                break
            if timeint[0] > (60*9 + i*t) or capacity-tmpcap == 1 :
                break
            timeint.popleft()
            tmpcap += 1
        capacity -= m

    if len(timeint) == 0 :
        answerint = last_time
    elif timeint[0] > last_time :
        answerint = last_time
    else :
        answerint = timeint[0]-1
        
    minute = answerint//60
    sec = answerint%60
    answer = "%02d"%(minute) + ":" + "%02d"%(sec)
    return answer