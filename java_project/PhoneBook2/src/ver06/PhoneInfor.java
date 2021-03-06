package ver06;

public abstract class PhoneInfor implements Infor {
	
	
	// 캡슐화 (변수보호)
	private String name;		// 이름
	private String phoneNum;	// 전화번호
	private String addr;		// 주소
	private String email;		// 이메일
	
	
	//object 클래스의 생성자를 호출
	public PhoneInfor(String name, String phoneNum, String addr, String email) {
		this.name = name;
		this.phoneNum = phoneNum;
		this.addr =addr;
		this.email = email;
	}
	
	
	// getter , setter
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPhoneNum() {
		return phoneNum;
	}

	public void setPhoneNum(String phoneNum) {
		this.phoneNum = phoneNum;
	}

	public String getAddr() {
		return addr;
	}

	public void setAddr(String addr) {
		this.addr = addr;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}
	
	// 정보 출력 하위 클래스에서 오버라이딩할 목적
		public void showInfor() {
			System.out.println("이름: "+name);
			System.out.println("전화: "+phoneNum);
			System.out.println("주소: "+addr);
			System.out.println("이메일: "+email);
		}

	public void showBasicInfor() {
			
		}

}
