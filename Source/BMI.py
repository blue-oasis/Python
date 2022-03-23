mon = eval(input("몸무게를 입력하세요(예, 74.3): "))
ki = eval(input("키를 입력하세요(예, 165, 177): "))
#몸무게, 키 입력함

#bmi 계산하기
kim = ki / 100

bmi = mon / (kim * kim)

#결과출력

msg = "당신은 "
if bmi < 18.5:
    msg += "저체중 "
elif bmi < 25:
    msg += "정상 "
else:
    msg+= "비만 "


print(msg + "입니다.")

print("bmi 수치는 " + str(bmi) + "입니다.")
