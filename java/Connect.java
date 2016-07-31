import java.sql.*;

public class Connect{

  static Connection con = null;

  public static void main(String[] args) {
    test();
  }

  public static void test(){
    connect();
  }

  public static Boolean connect(){
    final String host = "jdbc:mysql://localhost/garage_door";
    final String username = "piDoor";
    final String password = "1234";

    try{
      Class.forName("COM.MYSQL.JDBC.DRIVER");
      con = DriverManager.getConnection(host,username,password);
    }
    catch(SQLException e){
      System.out.println(e.getMessage());
    }
    catch(Exception e){
      System.out.println(e.getMessage());
    }

    if (con == null){
      System.out.println("not connected");
    }
    else{
      System.out.println("Connected");
    }


    return true;
  }
}
