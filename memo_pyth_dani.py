from platform import java_ver, python_branch
from re import A
from tokenize import Double, String
from turtle import goto


a.sort()
a.count('x')
a.find('x')
a.upper()
a.lower()
a.split() # a='life is'   -->   ['life','is']
len(a)
del a[0:3] #인덱스 설정후 삭제 딕셔너리에서는 키값을 써줘야한다.
a.append('x') #리스트 맨  마지막에 추가
a.sort()
a.reverse
a.index('x') #몇번째 인덱스인지 알려줌 0번째는 1로 쓰면서 시작
a.insert(0,'x')  #0의 위치에 x 를 삽입
a.remove('x') #리스트에서 첫번째로 나오는 단어x 또는 숫자를 삭제하는 함수
a.pop(1) #리스트에서 1번째 요소를 반환후 삭제한다
a.extend([4,5]) # a리스트끝에 4,5추가  == a+= [4,5]
a.replace('x','y')  # x를 y로 변경  

--------딕셔너리

del a[key]
a['x']  #키가 x인 벨류를 반환
a.get('x') #키가 x인 벨류를 반환
a.keys() / list(a.keys())  #a딕셔너리의 키를 모아 리스트로 반환 / 리스트로 반환
a.values() / list(a.values())
a.items() / list(a.items())
a.clear()


-----------set
set([1,2,3])    /   set('hello')         *** set(123) == set([1,2,3])  /  set('hello') == set('h''e''l''l''o') == set(['h','e','l','l','o'])       리스트로 감싸면 하나의 리스트가 된다. 
a & b   #교집합
a | b   #합집합
a - b   #차집합
a.add('x') #세트에 x 추가 리스트형식으로 사용시 리스트가 추가됨 주의 
a.update([1,2,3])   #정수는 리스트로 감쌈
a.remove('x')   #특정값 제거

-------------

a= [i+1 for i in range(10) if i<=10 == print('나무를{}번 베었습니다'.format(i+1))]


def dani(a):
    b=[] #반환값이 참인 것만 걸러저장
    for i in a:
        if i > 0:
            b.append(i)
    return b
print(dani([1,2,3,4,5,6]))

위문장을 filter 함수로 간단히  #필터 함수는 참인것만 걸러 저장

def dani(a):
    return x> 0
print(list(filter(dani,[1,2,3,4,5,6])))

--------------map 의 사용

def dani(num):
    a=[]
    for i in num:
        a.append(i*2)
    return a
a= dani([1,2,3,4])
print(a)
결과 = [2,4,6,8]


def dani(num): return num*2       # 간단히 줄여쓸수있다 
print(list(map(dani,[1,2,3,4])))
결과 = [2,4,6,8]


print(list(map(lambda a:a*2,[1,2,3,4])))  #lambda와 map사용으로 더 줄여쓸수 있다.
결과 = [2,4,6,8]

--------------랜덤

import random


random.random() 
#0~1사이 실수중 난수값을 무작위로 돌려 구해줌

random.randint(1,10)
#1~10 사이 정수중 난수 돌려구함

random.shuffle(변수)
#변수내 리스트의 항목을 무작위로 섞어놓는다.

