import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.io.FileWriter;
import java.io.IOException;
 
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class ConnectionHive {
	
	 private static String driverName = "com.amazon.hive.jdbc4.HS2Driver";
	  /**
	   * @param args
	   * @throws SQLException
	   */
	  public static void main(String[] args) throws SQLException {
	      try {
	      Class.forName(driverName);
	    } catch (ClassNotFoundException e) {
	      // TODO Auto-generated catch block
	      e.printStackTrace();
	      System.exit(1);
	    }
	    //replace "hive" here with the name of the user the queries should run as  
	      
	    Connection con = DriverManager.getConnection("jdbc:hive2://ec2-3-235-44-213.compute-1.amazonaws.com:10000/default", "hive", "");
	    PreparedStatement stmt ;//= con.createStatement();
	    
	    
	    JSONArray ListPays = new JSONArray();
	    
	    
		        	          
	    	String sql = " SELECT temp_covid.iso_code,"
		    		+ "AVG(temp_covid.new_cases),"
		    		+ "AVG(temp_covid.new_deaths),AVG(temp_covid.median_age),AVG(temp_covid.new_tests),AVG(temp_covid.hosp_patients) "
		    		+ "From temp_covid WHERE temp_covid.continent=? AND temp_covid.the_date>='2020-12-01' GROUP BY iso_code ";  
		        
	    stmt =con.prepareStatement(sql);
	    stmt.setString(1,"Oceania");
	    ResultSet result ;
	    result=stmt.executeQuery();
	    System.out.println("Début de l ecriture ");
	      
	  	  
	        while (result.next()) {
	        	// Pays
	            JSONObject pays1 = new JSONObject();
	            pays1.put("Code pays", result.getString(1));
	            pays1.put("Moyenne des cas", result.getString(2));
	            pays1.put("Moyenne des morts", result.getString(3));
	            pays1.put("Moyenne d'age", result.getString(4));
	            pays1.put("Nombre de tests en moyenne", result.getString(5));
	            pays1.put("Nombre d'hospitalisation en moyenne", result.getString(6));
	             
	            
	            ListPays.add(pays1);            
	            
	        }
	    
	        
	        
	        
	               
	         
	        //Write JSON file
	        try (FileWriter file = new FileWriter("/Users/massino/Desktop/Oceania.json",true)) {
	 
	            file.write(ListPays.toJSONString());
	            file.flush();
	 
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	        System.out.println("Fin de l ecriture");
        
       
	    
	  }
	
	
	

}
