import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
public class SSL_SererSide {
   public static void main(String[] args) throws IOException {
      Socket socket = null;
      InputStreamReader inputStreamReader = null;
      OutputStreamWriter outputStreamWriter = null;
      BufferedReader bufferedReader = null;
      BufferedWriter bufferedWriter = null;
      ServerSocket serverSocket;
      serverSocket = new ServerSocket(5000);
      while (true) {
         try {
            socket = serverSocket.accept();
            inputStreamReader = new InputStreamReader(socket.getInputStream());
            outputStreamWriter = new OutputStreamWriter(socket.getOutputStream());
            bufferedReader = new BufferedReader(inputStreamReader);
            bufferedWriter = new BufferedWriter(outputStreamWriter);

            while (true) {
               String msgFromClient = bufferedReader.readLine();
               System.out.println("Client: "+msgFromClient);
               bufferedWriter.write("message received.");
               bufferedWriter.newLine();
               bufferedWriter.flush();

               System.out.println("Server: "+bufferedReader.readLine());
               if ( msgFromClient.equalsIgnoreCase("BYE")){break;} 

            serverSocket.close();
            socket.close();
            }
            inputStreamReader.close();
            outputStreamWriter.close();
            bufferedReader.close();
            bufferedWriter.close();

         } catch (IOException e) {
            e.printStackTrace();
         }
      }
   }
}
