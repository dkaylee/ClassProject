<%@ page import="form.LoginData" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%

	LoginData loginData = (LoginData)request.getAttribute("login");

%>
    
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원 정보 출력</title>
</head> 
<body>

	<h1>회원이 작성한 데이터 출력</h1>
	
	<table>
		<tr>
		<td>ID</td>
		<td><%= loginData.getId() %></td>
		</tr>
		<tr>
		<td>PW</td>
		<td><%= loginData.getPw() %></td>
		</tr>
	</table>



</body>
</html>