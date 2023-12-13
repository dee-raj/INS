import java.io.*;
import java.net.Socket;
import java.util.Scanner;
public class SSL_ClientSide {
   public static void main(String[] args) {
      Socket socket = null;
      InputStreamReader inputStreamReader = null;
      OutputStreamWriter outputStreamWriter = null;
      BufferedReader bufferedReader = null;
      BufferedWriter bufferedWriter = null;
      try{
         socket = new Socket("localhost", 5000);
         inputStreamReader = new InputStreamReader(socket.getInputStream());
         outputStreamWriter = new OutputStreamWriter(socket.getOutputStream());
         bufferedReader = new BufferedReader(inputStreamReader);
         bufferedWriter = new BufferedWriter(outputStreamWriter);

         try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Here you start!:");
            while (true) {
               String msgToSend = scanner.nextLine();
               bufferedWriter.write(msgToSend);
               bufferedWriter.newLine();
               bufferedWriter.flush();

               System.out.println("Server: "+bufferedReader.readLine());
               if ( msgToSend.equalsIgnoreCase("BYE")){
                  break;
               }
            }
         }
      }catch(IOException e){
         System.out.println("Some error... "+e);
      }finally{
         try{
            if( socket != null)                       socket.close();
            if( inputStreamReader != null)            inputStreamReader.close();
            if( outputStreamWriter != null)           outputStreamWriter.close();
            if( bufferedReader != null)               bufferedReader.close();
            if( bufferedWriter != null)               bufferedWriter.close();
         }catch(IOException e){
            e.printStackTrace();
         }
      }
   }
}
