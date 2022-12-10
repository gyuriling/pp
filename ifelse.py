print('수를 입력하세요 : ')
a=input()

if type(a)==int:
    print('3 /', a, '=', 3/a)
else:
    print('{a}은 나눗셈에 이용할 수 없습니다.'.format(a))
    
