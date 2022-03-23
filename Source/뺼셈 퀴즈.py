import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)

if n1<n2 :
    n1, n2 = n2, n1

a = eval(input(str(n1) + " - " + str(n2) + \ "은/는 얼마입니까?"))


print(str(n1) + " - " + str(n2) + " = " + str(a) + \ "은/는", n1 - n2 == a, "입니다" )
