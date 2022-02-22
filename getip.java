import java.net.*;
class getip {
    public static void main(String[] args) {
        try {
            InetAddress addr = InetAddress.getLocalHost();
            System.out.println(addr.getHostAddress());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
  }