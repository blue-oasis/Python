import random

#컴터 할당

com = random.randint(0, 2)

#사람 입력
user = eval(input("가위 (0), 바위(1), 보(2) 를 입력하세요: "))

#승패 평가
if com == 0:
    if user == 0:
        print("컴퓨터는 가위, 당신도 가위, 비겼습니다.")
    elif user == 1:
        print("컴퓨터는 가위, 당신은 바위, 이겼습니다.")
    else:
        print("컴퓨터는 가위, 당신은 보, 졌습니다.")

elif com == 1:
    if user == 0:
        print("컴퓨터는 바위, 당신은 가위, 졌습니다.")
    elif user == 1:
        print("컴퓨터는 바위, 당신은 바위, 비겼습니다.")
    else:
        print("컴퓨터는 바위, 당신은 보, 이겼습니다.")

else:
    if user == 0:
        print("컴퓨터는 보, 당신은 가위, 이겼습니다.")
    elif user == 1:
         print("컴퓨터는 보, 당신은 바위, 졌습니다.")
    else:
         print("컴퓨터는 보, 당신은 보, 비겼습니다.")
