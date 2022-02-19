# 홀/짝을 고르시오
import random
# a = input("홀/짝을 고르세요")
#
# rnd = random.random() * 2 + 1
# com = int(rnd)
#
# if (com % 2 == 0 and a == "짝") or (com % 1 != 0 and a == "홀") :
#     print("승리하였습니다.")
# elif (com % 2 == 0 and a == "홀") or (com % 1 != 0 and a == "짝") :
#     print("패배하였습니다.")
# 기본적으로 mvc 패턴을 이용해서 코딩하자! 선언부/ 비즈니스 로직 / 뷰단

com = ""
me = ""
result = ""

me = input("홀/짝을 넣으세요")
rnd = random.random()

if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"
    
if com == me :
    result = "승리"
else :
    result = "패배"
    
print("컴", com)
print("나", me)
print("결과", result)
