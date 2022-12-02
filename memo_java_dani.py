---------------------------------(배열)스프링버퍼 사용 문자열 추가기능 
public class play {
 public static void main(String[] args) {
	 
	 StringBuffer a1 = new StringBuffer();
	 
	 a1.append("헬로");
	 a1.append(2); 
     a1.insert(0,33);  # 0 에다가 33을 대입해라
    	System.out.println(a1);
}
}
-------------------------------- 스프링 버퍼 없이 이런식으로 사용해도 상관은 없지만 수정이 불가하고 객체를 계속 생성하는식이라 잘 안쓴다.
String result = "";
result += "hello";
result += " ";
result += "jump to java";
System.out.println(result);

--------------------------------리스트 에서의 함수

a.add('x')
a.add(0,'x')
a.get(0)           0번째 인덱스 출력
a.size()           리스트 안의 인덱스 갯수출력
a.contains("x")    리스트 안에 x 가 있는지 파악후 boolean 으로 참,거짓 출력
a.remove("s")      S라는 객체(변수)를 삭제후 출력
a.remove(0)        0번째 인덱스를 삭제후 출력
a.sort(Comparator.natura10redr());     오름차순 정렬(순방향)
a.sort(Comparator.reverseOrder());     내림차순 정렬(역방향)
String 새로운변수 = String.join("", args);


---------------------------------HashMap 에서의 함수
a.put("s","x")     key와value 추가
System.out.println(map.get("x")        key"x" 입력시 value 값 출력
System.out.println(map.remove("x"));   key"x" 입력시 value값 출력 후 key와 value 가 삭제된다.
System.out.println(map.size());        key:value 세트 수를 출력해준다.
System.out.println(map.keySet());      맵의 모든 Keys 를 출력한다. 
    List<String> keyList = new ArrayList<>(map.keySet());     출력된 keys를 리스트로 변환 할 수 있다.


---------------------------------arrylist 
import java.util.ArrayList;
public class play {
 public static void main(String[] args) {

Arrylist a = new Arrlist
a.add("x")
System.out.println(a)   #출력결과 x




이렇게 사용해도 상관은없지만 제네릭스를 사용해서 추가하는게 좋다 <>안에 자료형만써주면된다. 위 형태로 입력시 나중에 함수 사용할때 형변환을 계속 해줘야한다.
import java.util.ArrayList;
public class play {
 public static void main(String[] args) {
	



ArrayList<Integer> a = new ArrayList<>()
a.add(333);
System.out.println(a);  #출력결과 333




 ArrayList<Integer> a = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5));
 System.out.println(a);    #Arrays.asList()를 추가하여 리스트 바로생성도 가능!!!!! 


----------------------------------HashMap  (python 의 딕셔너리와 비슷해보인다..)
import java.util.HashMap;
public class Sample {
    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<>();




---------------------------------형변환
public class Sample {
    public static void main(String[] args) {
        String num = "123";
        int n = Integer.parseInt(num);
        System.out.println(n);  // 123 출력
# 문자열을 정수로 변환했다.

public class Sample {
    public static void main(String[] args) {
        int n = 123;
        String num = "" + n;
        System.out.println(num);  // 123 출력
# 정수를 문자열로 변환했다.


---------------------------------if 조건문
boolean money = true;
if (money) {
    System.out.println("택시를 타고 가라");
}else {
    System.out.println("걸어가라");




    int money = 2000;
if (money >= 3000) {
    System.out.println("택시를 타고 가라");
}else {
    System.out.println("걸어가라");
}




    	#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라
public class paly {
    public static void main(String[] args) {
    	Scanner zz = new Scanner(System.in);
    	
    System.out.println("얼마있니");
    int a = zz.nextInt();   
    boolean okcard = true;
    
    if (a > 3000 || okcard ) {
    	System.out.println("택시타고가");
    }
    else {
    	System.out.println("걸어가");
    }
    }
    }




# if 문에서 contains 를 사용예제 python 의 in 이랑 비슷한것같다.
    ArrayList<String> pocket = new ArrayList<String>();
pocket.add("paper");
pocket.add("handphone");
pocket.add("money");

if (pocket.contains("money")) {
    System.out.println("택시를 타고 가라");
}else {
    System.out.println("걸어가라");
}





#else if 의 사용 python 의 elif 와 같다
boolean hasCard = true;
ArrayList<String> pocket = new ArrayList<String>();
pocket.add("paper");
pocket.add("handphone");

if (pocket.contains("money")) {
    System.out.println("택시를 타고 가라");
}else if(hasCard) {
    System.out.println("택시를 타고 가라");
}else {         
    System.out.println("걸어가라");
}


---------------------------------switch / case / break / default

#switch/case 문이다 while 문하고 조금 비슷해보인다 아래 예제에는 인풋을 먼저 3이라고 주어서 March 가 출력되었다.
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class paly {
    public static void main(String[] args) {

    	int month = 3;
        String monthString = "";
        switch (month) {
            case 1:  monthString = "January";
                     break;
            case 2:  monthString = "February";
                     break;
            case 3:  monthString = "March";
                     break;
            case 4:  monthString = "April";
                     break;
            case 5:  monthString = "May";
             		 break;
            default: monthString = "Invalid month";
                     break;
        }
        System.out.println(monthString);
    }
}




#위 예제를 스캐너로 입력 받아서 출력할 수 있게끔 바꾸었다.
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class paly {
    public static void main(String[] args) {
Scanner zz = new Scanner(System.in);
System.out.println("몇월을 출력해줄까");
int a= zz.nextInt();
    	int month = a;
        String monthString = "";
        switch (month) {
            case 1:  monthString = "January";
                     break;
            case 2:  monthString = "February";
                     break;
            case 3:  monthString = "March";
                     break;
            case 4:  monthString = "April";
                     break;
            case 5:  monthString = "May";
             		 break;
            default: monthString = "Invalid month";
                     break;
        }
        System.out.println(monthString);
    }
}


------------------클래스 사용
# return 을 사용해서 if 문 뒤 나의별명은 닉입니다는 출력되지 않는다
public class Sample {
    void sayNick(String nick) {
        if ("fool".equals(nick)) {
            return;
        }
        System.out.println("나의 별명은 "+nick+" 입니다.");
    }

    public static void main(String[] args) {
        Sample sample = new Sample();
        sample.sayNick("angel");
        sample.sayNick("fool");  // 출력되지 않는다.
    }
}


---------------------------------------------class


# 내가 만들어본 클래스이다
package exam;

import java.util.Scanner;

public class Scan {
	String aa;
	int power;
	int defence;
	String name;
	
void dani() {
	if (aa.equals("all")||aa.equals("ALL")) {
		System.out.println("이름:다니, 공격력:10, 방어력:20");
		System.out.println("이름:세니, 공격력:11, 방어력:21");}
	else {
	if (aa.equals("da")) {
		name = "dani";
		power = 10;
		defence = 20;}
	
	else if(aa.equals("se")) {
		name = "seni";
		power = 11;
		defence = 21;}?
	else {
		System.out.println("errer! Re");
		}
		System.out.println("name:"+name+"power:"+power+"defene:"+defence);	}}

public static void main(String[] args) {
	Scan game = new Scan();
	Scanner zz = new Scanner(System.in);
	
		System.out.println("캐릭터를 입력하세요 da/se/all  :");
	    game.aa = zz.next();
        System.out.println();
	    game.dani();







# 클래스 생성자 예제문이다 이게 파이썬과 가장 가까운듯해보인다.

class Car {
    private String modelName;
    private int modelYear;
    private String color;
    private int maxSpeed;
    private int currentSpeed;

    Car(String modelName, int modelYear, String color, int maxSpeed) {
        this.modelName = modelName;
        this.modelYear = modelYear;
        this.color = color;
        this.maxSpeed = maxSpeed;
        this.currentSpeed = 0;

    }
    public String getModel() {
        return this.modelYear + "년식 " + this.modelName + " " + this.color;
    }

}
public class Method02 {
  public static void main(String[] args) {
       Car myCar = new Car("아반떼", 2016, "흰색", 200); // 생성자의 호출
        # mycar.modelName="아반떼";
        # mycar.modelYear=2016;
        # mycar.color="흰색";
        # mycar.maxSpeed=200
        # 이런식으로 변수 설정해줘도 된다.


        System.out.println(myCar.getModel()); // 생성자에 의해 초기화되었는지를 확인함.
    }

}