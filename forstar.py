print('반복횟수를 입력하세요 : ', end="")
a= int(input())

if a<=0:
    print('0보다 작거나 같은 수는 입력할 수 없습니다.')


for a in range(a+1):
    for a in range(a):
        print('*', end="")
    print("")
