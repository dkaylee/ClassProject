package mvc.command;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MemberLoginCommand extends Command {



	@Override
	public String getViewPage(HttpServletRequest request, HttpServletResponse response) {
		// 사용자 요청을 처리, 응답에 필요한 데이터 request 속성에 저장, 응답에 필요한 설정
		// 이 요청의 응답 처리를 위한 view 페이지 경로를 반환
		String viewPage = null;
		
		// 사용자 요청 처리
		String result = "회원가입 페이지 입니다." + request.getRequestURI();
		
		// request  속성의 결과를 저장
		request.setAttribute("result", result);
		
		
		return "/view/member/regForm.jsp";
	}

}
