package mvc.command;


import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public abstract class Command {
	
	// 요청의 처리, 속성에 결과를 저장, view페이지로 경로를 반환
	public abstract String getViewPage(HttpServletRequest request, HttpServletResponse response);
	

}
