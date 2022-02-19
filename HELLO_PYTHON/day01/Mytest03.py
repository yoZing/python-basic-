a = input("첫 수를 넣으세요")
b = input("마지막 수를 넣으세요")
c = input("배수를 넣으세요")

aa = int(a)
bb = int(b)
cc = int(c)

arr = range(aa, bb + 1)

sum = 0;

for i in arr :
    if i % int(c) == 0 : 
        sum += i
    # else : pass

print(f"{a}에서 {b}까지 숫자 중 {c}의 배수의 합은 {sum}입니다.")
print("{}에서 {}까지 숫자 중 {}의 배수의 합은 {}입니다.".format(aa, bb, cc, sum))