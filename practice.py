
print(abs(-5))
print(pow(4,2)) # 4^2
print(max(5,12)) # 최대값
print(min(5,12)) # 최소값
print(round(5.12)) # 반올림
print(round(5.6)) # 반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

from random import *
print(random()) # 0.0 ~ 1.0 미만읜 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 값 생성

#로또 숫자 뽑기
print(randrange(1,46)) #1 ~ 46 미만의 값 생성
print(randint(1,45)) #1 ~ 45 이하의 값 생성 




# 모임 일정정하기
# 조건1: 랜덤으로 날짜 출력
# 조건2 : 월별 날짜는 28일 이내로 정함
# 조건3 : 매월 1~3일은 제외
# 출력 예제) 오프라인 모임 날짜는 매월 x일로 선정되었습니다.

date = randint(4, 28)
print("오프라인 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")
print(f"오프라인 모임 날짜는 매월 {date}일로 선정되었습니다.")
print("오프라인 모임 날짜는 매월 %d일로 선정되었습니다." %20)
print("오프라인 모임 날짜는 매월 %d일로 선정되었습니다." %date)

print("%s색 풍선, %s색 풍선" %("빨간", "파란"))
print("{}색 풍선, {}색 풍선".format("빨간", "파란"))
print("{1}색 풍선, {0}색 풍선".format("빨간","파란"))
print("{red}색 풍선, {blue}색 풍선".format(red="빨간",blue="파란"))