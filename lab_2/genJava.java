import java.security.SecureRandom;

/*
 * The Binary Random Generator class generates a random binary sequence
 * 128-bit long
 */
public class BinaryRandomGenerator {
    private static final int BYTE_LENGTH = 16; 

    public static void main(String[] args) {
        SecureRandom secureRandom = new SecureRandom();
        
        byte[] randomBytes = new byte[BYTE_LENGTH];
        secureRandom.nextBytes(randomBytes);
        
        StringBuilder binaryString = new StringBuilder();
        for (byte b : randomBytes) {
            String binaryByte = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            binaryString.append(binaryByte);
        }

        System.out.println("");
        System.out.println(binaryString.toString());
    }
}