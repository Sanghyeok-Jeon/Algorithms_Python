def timeToSec(lst):
    return int(lst[0])*3600 + int(lst[1])*60 + int(lst[2])

nowTime = timeToSec(list(input().split(':')))
missionTime = timeToSec(list(input().split(':')))

remainTime = missionTime - nowTime if missionTime >= nowTime else 24*60*60 + missionTime - nowTime

rtHH = remainTime // 3600
remainTime %= 3600
rtMM = remainTime // 60
remainTime %= 60

print('{:02d}:{:02d}:{:02d}'.format(rtHH, rtMM, remainTime))