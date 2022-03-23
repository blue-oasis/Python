import time

currentTime = time.time()

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60

totalMinute = totalSeconds // 60

currentMinute = totalMinute % 60

totalHours = totalMinute // 60

currentHours = totalHours % 24

print("현재 시간은", currentHours, ":", currentMinute, ":", currentSeconds)
