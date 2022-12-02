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


------------------------------------------------Scanner 의 사용 파이썬의 input 이랑 비슷한것같다..
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





---------------------------------------------사칙연산

        a=a+1;
    =   a+=1;
    =   a++;

곱하기 나누기 는 안된다.

---------------------------------------------형변환
float f1 =(float) 1.234;

---------------------------------------------연산자 비교 연산자에서 기준이되는 a1 ,a3 는 비교할 숫자보다 앞에 써주자! and 확률적으로 높은걸 앞에써서 비교해주자
import java.util.Scanner;

public class YMain6 {
public static void main(String[] args) {

Scanner jj = new Scanner(System.in);

System.out.println("나이 :");
int a1 = jj.nextInt();

System.out.println("키 :");
int a2 = jj.nextInt();

float a3=(a2/100);

boolean a4= (a1 > 3 && a3 >= 2);

System.out.printf("탈 수 있나요? %b",a4);
System.out.println(a3);

-------------------------------------------shift 시프트 연산자 : 다중선택
옮기다,이동하다 의 뜻
(십진수 << 정수 ) 의 형태 
<< : 앞에 있는 수를 2진수로 바꾸고, 뒤에있는 수만큼 왼쪽으로 밀어라.
     비어있는 (오른쪽) 칸 수를 0으로 채우고,2진수를 다시 10진수로 바꿔라.and

ex) 카페!
                       1
    24시간 : 1<<0 = 1
    와이파이 :1<<1 =2
    흡연실 : 1<<2 =4
    주차장 : 1<<3 =8 


    A매장 : 2
    B매장 : 8
    C매장 : 13
    D매장 : 6

-----------------------------------------삼항 연산자  
String c = (a > 20) ? "어서오세요":"나가";
System.out.printf("%s",c);



# 1상자에 축구공 6개 들어갈수있다 ex) 공49 -> 9개
System.out.println("축구공");
int a = zz.nextInt();
int b = a/6;
int c = (a%6 >=1) ? (a/6)+1:a/6;



if 문 보다 간결하게 쓸 수 있어서 좋다...! ! !!


------------------------------------------equals 는 python의 is 랑 비슷한 느낌?
Scanner zz = new Scanner(System.in);
System.out.println("이름이 뭐냐");
String a = zz.next();	
String name = "홍길동";
boolean a1 =(  a.equals(name));	
System.out.printf("이름이 같니? %b",a1);