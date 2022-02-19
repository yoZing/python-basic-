a = input("첫수를 적으세요")
b = input("마지막 수를 적으세요")
aa = int(a)
bb = int(b)

arr = range(aa, bb + 1)

sum = 0;
for i in arr :
    sum += i
    
print(a + "부터" + b + "까의 합계는", sum, "입니다.")  
print(f"{a}에서 {b}까지의 합계는 {sum}입니다.")
print("{}에서 {}까지의 합계는 {}입니다.".format(aa, bb, sum))    
      
    