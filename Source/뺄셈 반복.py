import random
import time

correctcount = 0
count = 0
question = eval(input("문제의 개수를 결정하세요: "))

strattime = time.time()

while count < question:
    n1 = random.randint(1, 15)
    n2 = random.randint(1, 15)

    if n1 < n2 :
        n1, n2 = n2, n1
    
    answer = eval(input(str(n1) + " - " + str(n2) + "은/는 얼마입니까? "))

    if n1 - n2 == answer:
        print("맞았습니다.")
        correctcount += 1
    else:
        print("틀렸습니다.", n1, "-", n2, "는",  n1 - n2, "입니다.")
    count += 1

endtime = time.time()
testtime = int(endtime - strattime)
print("정답의 개수는", question, "개 중", correctcount,"개 입니다.", "수행시간은 ", testtime, "초 입니다.")
