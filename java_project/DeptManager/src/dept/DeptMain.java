package dept;

import java.util.Scanner;

public class DeptMain {

	public static void main(String[] args) {
		
		DeptManager manager = new DeptManager();
		
		Scanner sc = new Scanner(System.in);
		
		// 데이터 베이스 드라이버 로드
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//manager.insertDept();
			//manager.editDept();
			//manager.delDept();
			//manager.listDept();
			//manager.searchDept();
			
			while(true) {
			
			System.out.println("부서관리 메뉴 입력해주세요");
			System.out.println("1. 입력, 2. 수정, 3. 삭제, 4. 전체리스트, 5. 검색, 6.종료");
			System.out.println("------------------------------------------------");
			
			
			String select = sc.nextLine();
			
			switch (select.charAt(0)) {
			case '1':
				manager.insertDept();
				break;
			case '2':
				manager.editDept();
				break;
			case '3':
				manager.delDept();
				break;
			case '4':
				manager.listDept();
				break;
			case '5':
				manager.searchDept();
				break;
			case '6':
				System.out.println("프로그램 종료");
				return;
			
			
			}
			
		}
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

}
