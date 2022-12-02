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



==================================
java 의 특징 
세심하게 하나하나 손봐줘야한다.
나중에 다른 언어를 배울때 습득하기가 편하다.
고급언어에서 저급언어 순으로
python (빅테이터,ai)
jQuery
javaScript
java  
Go
고급언어는 컴퓨터가 자동으로 처리해주는게많아서 고급언어이고
저급언어는 개발자가 일일히 처리를 해준다해서 저급언어이다.
좋고 나쁘고는 없다.

자바설치시
(JDK {java Delopment Kit}를 설치해야함) 
1.openjdk github 구글 검색 (https://github.com/ojdkbuild/ojdkbuild) 
2.java-1.8.0-openjdk-1.8.0.332-1.b09.ojdkbuild.windows.x86_64.msi (sha256) 다운
3.https://www.eclipse.org/downloads/     이클립스 들어가서 맨아래 Download Packages 작은글씨로된거 클릭
4. 오른쪽아래 more downlode 에서 대충 최근거 클릭
5.Eclipse IDE for Enterprise Java and Web Developers 오른쪽 윈도우로다운
6. 이클립스 알집은 아직 풀지않는다
7. 메뉴에서 cmd 입력 java -version 입력후 jdk가 설치가 잘되었는지 확인
8. 이클립스 알집풀고 이클립스 실행 
9. workspace 폴더 설정 browser 로 폴더 생성
10.위 메뉴에서 윈도우탭 맨아래 프리퍼런시스 클릭 왼쪽 자바탭에서 installed JREs 를들어가 내장되어있는것을 삭제 후 add 하여 설치한 JDK  C드라이브에 들어가면 ojdkbuild안에 
   java 1.8.0 어쩌고저쩌고 폴더 선택후 피니쉬 설정 후 어플라이
11. Compiler 설정 들어가서 숫자를 1.8버전이니 1.8로 클릭 후 어플라이
12. General 에 있는 Workspace 로 들어가서 Text file encoding 에 Other 에서 EUC-KR 로 입력 후 어플라이 한후 어플라이앤드 크로스 누르면 설정 완료.


------------------------------------------이클립스 단축키
// : 한줄주석
/* : 여러줄 주석
/**: 다른사람들에게 보여주기 위한 설명서 es) @auther dani , @version 1.1.10 등
/  :  Slash
\  :  역슬래시
ctrl + s 파일저장
ctrl + a 전체 선택
ctrl + m 화면 비율 조정
ctrl + shift + /  드래그 해놓은 줄 주석처리 
ctrl + alt + 방향키 위아래  :  현재 줄 기준으로 위아래 복사
alt + 방향키 위아래 :  해당줄을 위아래로 이동
ctrl + shift + +/-  : 글자 크기 조정
ctrl + d  :  현재 줄 삭제
ctrl + spacebar  :  드래그 한 줄 자동완성
ctrl + shift + f  :  줄정리
ctrl + f11  :  실행기능

-----------------------------------------------java print 의 형태
println  :  콘솔창에 글자를 출력하고 줄바꿈 (제일많이 사용) 괄호안에 값이 없으면 줄바꿈역할
print  :  콘솔창에 글자를 출력함 줄바꿈 역할x (덜사용)
printf  :  콘솔창에 형식을 지정해서 글자를 출력 (ex:소수점 자릿수지정)

-----------------------------------------------이스케이프 문자
	Escape Sepuence (이스케이프 문자)
		     : 특수한 문자나 기능을 표현할때 역슬래시를 사용
\t  :  줄을 맞추는 용도
\n  :  뉴 라인 (줄만 맞추는 용도)
\r  :  Carriage Return (커서를 맨 앞으로 이동)
\r\n  :  커서를 맨앞으로 이동해서 줄을 맞춘다 (Enter키 기능)
\b  :  Backspace 키 기능을 해준다.
\0  :  빈칸 한칸 (Space키 기능)



------------------------------------------------JAVA 변수
변수선언 (만든다) : RAM 에 공간을 확보해서 무언가를 담을수 있는 공간을 만든다.  
    * 자료형 변수명; 의 형태를 변수를 선언 했다 라고 표현

변수초기화 : 변수에 값을 넣어야한다  자료형은 변수가 어떤값으로 저장할지의 형태이고 , 변수명은 말그대로 변수의 이름이다.
    *변수명=값; 의 형태로 표현한다.

변수 선언과 초기화를 동시에
    *자료형 변수명 = 값;

변수명 짓는 규칙
    숫자X 특수문자X 띄어쓰기X 자바문법예약어X 아래하이픈ex: _int 처럼 사용하면 에러 방지
    *변수명만봐도 뭔지 알 수 있게 선언

------------------------------------------------
String
int
Double


------------------------------------------------Scanner 파이썬의 input 이랑 비슷한것같다..
Scanner : Java 에 내장되어있는 기능 중 하나
Import 를 하여야하며 Scanner 기능을 사용하려면 조건이 하나 필요한데 
new ~~ : 라는 객체를 써야한다.
Scanner 는 화면 (이클립스의 콘솔창) 으로 데이터를 입력받는 기능.


import java.util.Scanner;  #자동으로 뜬다.

public class KIMain3 {
public static void main(String[] args) {
	Scanner zzz = new Scanner(System.in);

	System.out.println("떡볶이: ");
	int da = zzz.nextInt();
	System.out.println("순대: ");
	int dada=zzz.nextInt();
	System.out.println("어묵: ");
	int dadada=zzz.nextInt();
	System.out.println("튀김: ");
	int dadadada=zzz.nextInt();
	System.out.println("라면: ");
	int dadadadada=zzz.nextInt();
	System.out.println("생선: ");
	int dadadadadada=zzz.nextInt();
	
	System.out.println("*************************");
	System.out.println("*\t메뉴판\t\t*");
	System.out.println("*************************");
	System.out.printf("*떡볶이 :\t  %,d\t*\n",da);
	System.out.printf("*순대   :\t  %,d\t*\n",dada);
	System.out.printf("*어묵   :\t  %,d\t*\n",dadada);
	System.out.printf("*튀김   :\t  %,d\t*\n",dadadada);
	System.out.printf("*멸치   :\t  %,d\t*\n",dadadadada);
	System.out.printf("*생선   :\t  %,d\t*\n",dadadadadada);
	System.out.println("*************************");
	System.out.printf("   합계:\t\t%d  ",da+dada+dadada+dadadada+dadadadada+dadadadadada);
	zzz.close();