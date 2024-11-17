

# 추첨 이벤트 20명의 참가자중 1명은 치킨 3명은 커피 쿠폰을 받는다.
# 20명의 참가자의 아이디는 1 - 20
# 무작위 추천 & 중복불가
# random 모듈의 shuffle과 sample 사용

from random import *

users = range(1,21)
users = list(users)
print(users)

shuffle(users)
print(users)

winners = sample(users,4)
print(winners)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하 합니다. --")