import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__stratTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int(1000 * (self.__endTime - self.__startTime))

def main():
    size = 1000000

    stopWatch = StopWatch()
    
    sum = 0
    for i in range(1, size + 1):
        sum += i

    stopWatch.stop()

    print("1부터 1000000까지 더하는데 소요된 시간은", stopWatch.getElapsedTime(), "밀리초 입니다.")

main()
