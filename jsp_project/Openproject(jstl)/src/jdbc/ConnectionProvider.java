package jdbc;

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;

public class ConnectionProvider {
	
	public static Connection getConnection() throws SQLException {
		
		Connection conn=null;
		
		// 2. DB 연결 : Connection 객체를 얻기
	 	String jdbcUrl = "jdbc:mysql://localhost:3306/open?serverTimeZone=UTC";
		String user = "dk";
		String password = "dk";
		
		conn = DriverManager.getConnection(jdbcUrl, user, password);
		
		return conn;
	}
}
