package first;

public class Work3 {

	public static void main(String[] args) {
		
		/*
		 문제1.
		int 형 변수 num1, num2, num3가 각각 10,20,30 으로 초기화 되어 있다.
		다음문장을 실행하면 각각 변수에는 어떠한 값이 저장되겠는가?
		num1=num2=num3 ; 확인 하는 코드를 작성하고, 그 결과에 대해 설명.
		*/
		
		//num1,2,3 모두 30이된다. 대입 방향이 오른쪽에서 왼쪽으로 진행되기때문이다.
		
		int num1=10;
		int num2=20;
		int num3=30;
		
		num1=num2=num3;
		
		System.out.println("num1 = "+num1);
		System.out.println("num2 = "+num2);
		System.out.println("num3 = "+num3);
		
		
		/*
		 문제2.
		 수학식 {{(25x5)+(36-4)}-72}/5 의 계산결과를 출력하는 프로그램 작성.
		 */
		
		int result = (((25*5)+(36-4))-72)/5;
		System.out.println("{{(25x5)+(36-4)}-72}/5 = "+ result);

		
		/*
		문제3.
		3+6, 3+6+9, 3+6+9+12 의 연산을 하는 프로그램 작성.
		단. 덧셈 연산의 횟수 최소화
		*/
		
		int oper1 = 3+6;
		int oper2 = 3+6+9; // oper2 = oper1+9
		int oper3 = 3+6+9+12; // oper3 = oper2+12
		
		oper2 = oper1 + 9;
		oper3 = oper2 + 12;
		
		
		/*for(int i=3; i<13; i+=3) {
			sum=sum+i;
		}
		
		System.out.println("3+6+9+12 = "+sum);
		*/
		
		
		
		/*
		문제4.
		a= {{(25+5)+(36/4)}-72}*5, b= {{(25x5)+(36-4)}-71}/4, c=(128/4)*2 일 때
		a>b>c 가 참이면 true 아니면 false를 출력하는 프로그램 작성
		*/
		
		int a = (((25+5)+(36/4))-72)*5;
		int b = (((25*5)+(36-4))-71)/4;
		int c = (128/4)*2;
	
		// a>b>c
		boolean check = a>b && b>c;
		
		System.out.println(check);
		
		
	}
}