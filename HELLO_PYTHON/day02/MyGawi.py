# 가위 바위 보 게임 만들기
# 선언부
import random
me = ""
com = ""
result = ""

# rnd = int(random.random() * 3)
# arr = ["가위", "바위", "보"]
# me = input("가위/바위/보 중 하나를 입력하세요")
# com = arr[rnd]
# if (me == "가위" and com == "보") or (me == "바위" and com == "가위") or (me == "보" and com == "바위") :
#     result = "플레이어 승리!"
# elif (me == "가위" and com == "바위") or (me == "바위" and com == "보") or (me == "보" and com == "가위") :    
#     result = "플레이어 패배!"
# else :
#     result = "무승부!"
#
# print("me", me)
# print("com", com)
# print("결과", result)

mine = input("가위/바위/보를 넣으세요")
rnd = random.random()
if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else :
    com = "보"
    
if com == "가위" and mine == "가위": result = "비김"
if com == "가위" and mine == "바위": result = "짐"
if com == "가위" and mine == "보": result = "이김"

if com == "바위" and mine == "바위": result = "비김"
if com == "바위" and mine == "보": result = "짐"
if com == "바위" and mine == "가위": result = "이김"

if com == "보" and mine == "보": result = "비김"
if com == "보" and mine == "가위": result = "짐"
if com == "보" and mine == "바위": result = "이김"

print("mine", mine)
print("com", com)
print("결과", result)