package first;

import java.util.Scanner;

public class ExamFlowControl {

	public static void main(String[] args) {
		
		//Ctrl+Shift+O -> 자동 import
		Scanner s = new Scanner(System.in);
		
//		[1] 다음의 문장들을 조건식으로 표현하라.

//		1. int형 변수 x가 10보다 크고 20보다 작을 때 true인 조건식
		int x = 15;
		boolean chk1 = x > 10  && x < 20;
		System.out.println("int형 변수 x가 10보다 크고 20보다 작을때 true인 조건");
		System.out.println("x > 10  && x < 20"+chk1);
		
//		2. char형 변수 ch가 공백이나 탭이 아닐 때 true인 조건식
		char ch = 'K';
		boolean chk2 = ch != ' ' || ch != '\t';
		boolean chk22 = !(ch == ' ' && ch == '\t');
		
		System.out.println("2. char형 변수 ch가 공백이거나 탭이 아닐때 true인 조건식");
		System.out.println("ch != ' ' || ch != '\\t' : "+chk2);
		System.out.println("chk22 = !(ch == ' ' && ch == '\\t' : "+chk22);
		
//		3. char형 변수 ch가 ‘x' 또는 ’X'일 때 true인 조건식
		ch = 'x';
		boolean chk3 = ch=='x' || ch=='X';
		System.out.println("3. char형 변수 ch가 ‘x' 또는 ’X'일 때 true인 조건식");
		System.out.println("ch=='x' || ch=='X' : "+chk3);
		
//		4. char형 변수 ch가 숫자(‘0’~‘9’)일 때 true인 조건식
		ch = '9';
		boolean chk4 = ch>='0' && ch<='9';
		System.out.println("char형 변수 ch가 숫자(‘0’~‘9’)일 때 true인 조건식");
		System.out.println("ch>='0' && ch<='9' : "+chk4);

//		5. char형 변수 ch가 영문자(대문자 또는 소문자 또는 숫자)일 때 true인 조건식
		ch = 'A';
		boolean chk5 = ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z' || chk4; // chk4 숫자
		System.out.println("char형 변수 ch가 영문자(대문자 또는 소문자)일 때 true인 조건식");
		System.out.println("ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z' : "+chk5);

//		6. int형 변수 year가 400으로 나눠떨어지거나 또는 4로 나눠떨어지고 100으로나눠떨어지지않을 때 true인 조건식
		int year = 400;
		boolean chk6 = year % 400 == 0 || year%4 == 0 && year%100 != 0;
		System.out.println("int형 변수 year가 400으로 나눠떨어지거나 또는 4로 나눠떨어지고 100으로나눠떨어지지않을 때 true인 조건식");
		System.out.println("year % 400 == 0 || year%4 == 0 && year%100 != 0 : " + chk6);
		 
//		7. boolean형 변수 powerOn가 false일 때 true인 조건식
		boolean powerOn = false;
		boolean chk7 = !powerOn;
		System.out.println("boolean형 변수 powerOn가 false일 때 true인 조건식");
		System.out.println("!powerOn : " + chk7);

//		8. 문자열 참조변수 str이 “yes”일 때 true인 조건식
		String str = "yes";
		boolean chk8 = str == "str";		// 참조값 비교
		boolean chk88 = str.equals("str");	// 저장하는 문자열을 비교
		System.out.println("8. 문자열 참조변수 str이 “yes”일 때 true인 조건식");
		System.out.println("str == \"str\" : " + chk8 );
		System.out.println("str.equals(\"str\"; : " + chk88);
		
//		[2] 1부터 20까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오
		System.out.println("\n============");
		
		int sum = 0;
		
		for(int i=0; i<21; i++) {
			if(!(i%2 == 0 || i%3 == 0)) {
				System.out.println(i);
				sum += i;
			}
		}
		System.out.println("총합을 구하시오 : " + sum);

//		[3] 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.
		System.out.println("\n============");

		// 1 sum -> 0 + (sum+1)
		// 1+(1+2) -> sum +(sum+2)
		// 1+(1+2)+(1+2+3) -> sum + (sum+3)
		// 합 -> sum
		
		sum = 0 ;
		int n = 1;
		int beforeSum = 0;
		
		for(int i=1; i<10; i++) {
			beforeSum += i;
			sum = sum+(sum+beforeSum);
			
		}
		System.out.println(sum);

		 

//		[4] 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이되는지 구하시오.
		//몇가지 더해야
		//총합이 100이상되는지
		System.out.println("\n문제 4번============");
		n=1;
		sum=0;
		while(true) {
			int num = n%2==0?-n:n;
			//System.out.println(num);
			sum = sum + num;
			
			if(sum>=100) {
				System.out.println(n + "을 더했을때 100이상인"+ sum + "이 됩니다.");
				break;
			}
			
			n++;
		}
		
//		[5] 다음의 for문을 while문으로 변경하시오.
		
//		[6] 두 개의 주사위를 던졌을 때, 눈의 합이 6이 되는 모든 경우의 수를 출력하는 프로그램을작성하시오.
//		10A + B + 10 B + A = 99
//		11A + 11B =99
//		A+B=99-22=77
		
		// 눈의 합이 6이다. dic1 + dice2 =6 -> dice2 =>
		// 주사위에서 발생할 수 있는 수의 범위 ->1-6 반복 범위
		
		System.out.println("\n문제 6번============");
		for(int i=1; i<6; i++) {
			System.out.print("첫번째 주사위가 "+i+"일때, ");
			System.out.println("두번째번째 주사위는 "+(6-i));
		}
		
//		[7] Math.random()을 이용해서 1부터 6사이의 임의의 정수를 변수 value에 저장하는 코드를완성하라. 
//		(1)에 알맞은 코드를 넣으시오.
		System.out.println("\n문제 7번============");
		int value = (int)(Math.random()*6)+1;
		System.out.println("value:" + value);
		
		
//		[8] 방정식 2x+4y=10의 모든 해를 구하시오. => x+2y=5
//		단, x와 y는 정수이고 
//		각각의 범위는 0<=x<=10,  0<=y<=10 이다.
//				[실행결과]
//				x=1, y=2
//				x=3, y=1
//				x=5, y=0
		
		System.out.println("\n문제 8번============");
		
		for(x=0; x<=10; x++ ) {
			for(int y=0; y<=10; y++) {	
				//if(2*x+4*y == 10) {
				if(x+2*y == 5) {
					System.out.println("x=" + x + ", y=" + y);
				}
			}
		}
		
		
//		[9] 숫자로 이루어진 문자열 str이 있을 때, 각 자리의 합을 더한 결과를 출력하는 코드를완성하라.
//		만일 문자열이"12345"라면, ‘1+2+3+4+5’의 결과인 15를 출력이 출력되어야 한다. (1)에 알맞은코드를 넣으시오.
//		[Hint] String클래스의 charAt(int i)을 사용
//		'0' = 48 / '1' = 49		
		
		System.out.println("\n문제 9번============");
		
		str = "12345";
		int cNum = Integer.parseInt(str); //문자열을 숫자타입으로 바꿔줄때 사용
		sum = 0;

		for(int i=0; i < str.length(); i++) {
			System.out.println(str.charAt(i));
			sum += str.charAt(i)-'0'; // 49-48, 50-48, 51-48...
		}

		System.out.println("sum="+sum);
		
		
//		[10] int타입의 변수 num 이 있을 때, 각 자리의 합을 더한 결과를 출력하는 코드를 완성하라. 
//		만일 변수 num의 값이 12345라면, 
//		‘1+2+3+4+5’의 결과인 15를 출력하라. (1)에 알맞은 코드를넣으시오.
//		[주의] 문자열로 변환하지 말고 숫자로만 처리해야 한다.
		
		System.out.println("\n문제 10번============");
		
		// 자리수 구하기
		// num%10 => 1의 자리수
		// num/10 => 10의 자리수가 1의 자리수가 된다.
		// 반복의 조건은 num>0
		
		int num = 12345;

		sum = 0;

		while(num>0) {
			System.out.println(num);
			sum = sum + (num%10);
			num = num / 10;
		}
		
		System.out.println("sum="+sum);

		
//		[11] 피보나치(Fibonnaci) 수열(數列)은 앞을 두 수를 더해서 다음 수를 만들어 나가는수열이다. 
//		예를 들어 앞의 두 수가 1과 1이라면 그 다음 수는 2가 되고 그 다음 수는 1과 2를더해서 3이 되어서
//		1,1,2,3,5,8,13,21,... 과 같은 식으로 진행된다.
//		1과 1부터 시작하는피보나치수열의 10번째 수는 무엇인지 계산하는 프로그램을 완성하시오.

		System.out.println("\n문제 11번============");
		int num1 = 1;
		int num2 = 1;
		int num3 = 0; // 세번째 값

		System.out.print(num1+","+num2);

		for (int i = 0 ; i < 8 ; i++ ) {
			num3 = num1 + num2;
			System.out.print(", "+num3);

			num1 = num2;
			num2 = num3;
			}
		
//		[13] 다음은 주어진 문자열(value)이 숫자인지를 판별하는 프로그램이다. 
//		(1)에 알맞은 코드를넣어서 프로그램을 완성하시오.
		
		System.out.println("\n문제 13번============");
		
		str = "12o34";
		ch = ' ';
		boolean isNumber = true;
		// 반복문과 charAt(int i)를 이용해서 문자열의 문자를
		// 하나씩 읽어서 검사한다.

		for(int i=0; i < str.length() ;i++) {
			ch = str.charAt(i);
			if(!(ch>='0'&&ch<='9')) {
				isNumber = false;
				break;
			}
		}
		if (isNumber) {
			System.out.println(str+"는 숫자입니다.");
		} else {
			System.out.println(str+"는 숫자가 아닙니다.");
		}
		
//		[14] 다음은 숫자 맞추기 게임을 작성한 것이다.
//		1과 100사이의 값을 반복적으로 입력해서컴퓨터가 생각한 값을 맞추면 게임이 끝난다. 
//		사용자가 값을 입력하면, 
//		컴퓨터는 자신이 생각한값과 비교해서 결과를 알려준다.	=>	비교 연산 출력 
//		사용자가 컴퓨터가 생각한 숫자를 맞추면 게임이 끝나고 몇 번만에 숫자를 맞췄는지 알려준다. 
//		(1)~(2)에 알맞은 코드를 넣어 프로그램을 완성하시오.	
		
		System.out.println("\n문제 14번============");
		
		// 1~100사이의 임의의 값을 얻어서 answer에 저장한다.
		int answer = (int)(Math.random()*100)+1;
		int input = 0; // 사용자입력을 저장할 공간
		int count = 0; // 시도횟수를 세기위한 변수

		// 화면으로 부터 사용자입력을 받기 위해서 Scanner클래스 사용

		do {

		count++;
		System.out.print("1과 100사이의 값을 입력하세요 :");
		input = s.nextInt(); // 입력받은 값을 변수 input에 저장한다.
		
		// 사용자가 입력한 값을 answer와 비교해서 결과를 출력
		// 큰수다!, 작은 수다!, 맞췄다!
		if(answer>input) {
			System.out.println("더 큰 수입니다.");
		} else if(answer<input) {
			System.out.println("더 작은 수입니다.");
		} else {
			System.out.println(count+"회 맞추셨습니다. 게임을 종료합니다.");
			break;
		}
		
		} while(true); // 무한반복문
		
		
//		[15] 다음은 회문수를 구하는 프로그램이다. 
//		회문수(palindrome)란, 숫자를 거꾸로 읽어도앞으로 읽는 것과 같은 수를 말한다. 
//		예를 들면 ‘12321’이나 ‘13531’같은 수를 말한다. (1)에알맞은 코드를 넣어서 프로그램을 완성하시오.
//		[Hint] 나머지 연산자를 이용하시오.
		
		System.out.println("\n문제 15번============");
		
		int number = 913319;
		int tmp = number;
		int result =0; // 변수 number를 거꾸로 변환해서 담을 변수
		
		while(tmp != 0) {

		result = result * 10 + (tmp % 10);
		// 1 -> 1*10+2 -> (1*10+2)*10+3 -> 123*10+2 -> 1232*10+1
		tmp /= 10; 		// 12321 -> 1232 -> 123 -> 12 -> 1 -> 0

		}

		if(number == result)
			System.out.println( number + "는 회문수 입니다.");
		else
			System.out.println( number + "는 회문수가 아닙니다.");
	
		
	
		
		
	}

}
