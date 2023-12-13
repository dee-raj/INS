package caesercipherprac1;
import java.util.Scanner;

public class Caesercipher {
    public static void main(String ins[]){
        Scanner sc=new Scanner(System.in);
        String msg,enCryptedMsg="";
        int key;
        char ch;
        System.out.println("Enter a message: ");
        msg=sc.nextLine();
        System.out.println("Enter key: ");
        key=sc.nextInt();
        
        for(int i=0; i<msg.length(); i++){
            ch=msg.charAt(i);
            if (ch >= 'a' && ch <= 'z'){
                ch = (char)(ch + key);
                
                if (ch > 'z'){
                    ch = (char)(ch - 'z' + 'a' - 1);
                }
                enCryptedMsg += ch;
            }
            else if (ch >= 'A' && ch <= 'Z'){
                ch = (char)(ch + key);
                
                if (ch > 'Z'){
                    ch = (char)(ch - 'Z' + 'A' - 1);
                }
                enCryptedMsg += ch;
            } 
        }
        System.out.println("Encrypted message: "+enCryptedMsg);
        sc.close();
    }
}
