// ping an ip address
import java.net.*;
class getip_website {
    public static void main(String[] args) {
        try {
            InetAddress addr = InetAddress.getByName("www.google.com");
            System.out.println(addr.getHostAddress());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}