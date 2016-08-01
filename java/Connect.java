import java.net.URL;
import java.net.URLConnection;
import java.io.*;
import java.util.HashMap;


public class Connect {
  private static HashMap<String,Integer> status;

  public static void main(String[] args){

    status = new HashMap<String,Integer>();
    try{
      URL url = new URL("http://localhost/garage_door/webpage/api/get_state.php");
      URLConnection connection = url.openConnection();

      InputStream in = connection.getInputStream();
      BufferedReader res = new BufferedReader(new InputStreamReader(in, "UTF-8"));

      String inputLine= res.readLine();
      res.close();

      System.out.println(inputLine);
      status = new HashMap<String,Integer>(inputLine);
    }//end try
    catch(Exception e){
      System.err.println(e.getMessage());
    }//end catch

  }//end main
}//end class
