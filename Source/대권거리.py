import math

x1, y1 = eval(input("첫 번째 도시의 위도와 경도를 입력하세요: "))
x2, y2 = eval(input("두 번째 도시의 위도와 경도를 입력하세요: "))

d = 6400 * math.acos(math.sin(math.radians(x1)) * \
     math.sin(math.radians(x2)) + math.cos(math.radians(x1)) *\
     math.cos(math.radians(x2)) * math.cos(math.radians(y1-y2)))

print("두 도시의 대권거리는", d, "km 입니다.")

                    
