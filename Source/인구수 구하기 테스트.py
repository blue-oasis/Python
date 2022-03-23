korea = 51761891 #현재 인구수
y = 365*(24*3600) #1년을 초로 변환 365일*(24시간*60분의 초수 3600)
bith = y // 17   #1년 출생수
deth = y // 12 #1년 사망수
inkorea = y // 87  #1년 입국수
outkorea = y // 231 #1년 출국수

n = eval(input("년 수를 입력하세요 : "))

x1 = korea + (n * bith) 
x2 = x1 - (n * deth)
x3 = x2 + (n * inkorea)
x4 = x3 - (n * outkorea)

print(n, "년 후의 인구는", x4, "입니다.")
