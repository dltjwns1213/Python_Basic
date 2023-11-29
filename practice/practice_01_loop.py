# 문제1) 입력 된 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#    print(f"{dan}x{i}={dan*i}")

# 문제2) 2단부터 9단까지 출력 => 중첩 for
print("="*100)
for i in range(2, 10):
   for j in range(1, 10):
       print(f"{i}x{j}={i*j}")

# 문제3) List a의 평균값을 계산하세요.
print("="*100)
a = {1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4}
total = 0
for num in a:
    total += num
length = len(a)
result = total / length
print(round(result, 2))

# 문제4) List b에서 최소값 찾기!
print("="*100)
b = [22, 1, 4, 7, 98]
num_min = b[0]
for num in b:
    if num < num_min:
        num_min = num
print(num_min) # 1 출력

# 문제5) List c의 최소값, 최대값 찾기
print("="*100)
c = [2, 5, 7, 1, 8]
num_min = c[0]
num_max = c[0]
for num in c:
    if num < num_min:
        num_min = num
    if num > num_max:
        num_max = num
print(num_min) # 1 출력
print(num_max) # 8 출력

print("="*100)
# 사용자가 입력한 값 1, 2, 3 통과
# 아닌 경우 다시 입력하도록
num = int(input("값: "))
# if 4 > num > 0: # num = 1, 2, 3
if num in [1, 2, 3]:
    pass
else:
    print("1, 2, 3의 값만 입력하세요.")

# 문제 6)
print("="*100)
count = 0
while True:
    if count >= 3:
        print("프로그램을 사용할 수 없습니다.")
        break
    m = int(input("값: "))
    if m in [1, 2, 3]:
        print(f"{m}을 입력하셨습니다.")
        break
    else:
        print("1, 2, 3의 값만 입력해주세요.")
        count += 1

# 문제 7)
print("="*100)
total = 0
for num in range(1, 101):
     total += num
print(f"총합(for): {total}")
print("="*100)
max = 100
total = 0
i = 1
while i<=max:
    total+=i
    i+=1
print(total)

print("="*100)
num = 0
total = 0
while True:
    num += 1
    if num == 101:
        break
    total += num
print(f"총합(while): {total}")
