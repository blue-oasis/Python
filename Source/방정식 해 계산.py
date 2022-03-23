import math
a, b, c = eval(input("a, b, c의 값을 입력하세요: "))

h = (b ** 2) - (4 * a *c) #판별식

if h > 0:
    h1 = (-b + math.sqrt(h)) / (2 * a)
    h2 = (-b - math.sqrt(h)) / (2 * a)
    print("실수 해는", h1,"과/와", h2, "입니다.")
elif h == 0:
    h1 = (-b + math.sqrt(h)) / (2 * a)
    print("실수 해는", h1, "입니다.")
else:
    print("이 방정식의 실수 해 존재하지 않습니다.")
