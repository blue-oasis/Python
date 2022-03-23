import random

number = random.randint(0, 100)

print("0과 100 사이 미지의 숫자를 맞혀보세요")
guess = -1
while guess != number:
    guess = eval(input("얼마일까요?: "))

    if guess == number:
        print("맞습니다. 미지의 숫자는" , number , "입니다.")
    elif guess > number:
        print("입력한 값이 너무 큽니다.")
    else:
        print("입력한 값이 너무 작습니다.")

