import java.lang.Math;

public class sqrtTime {

  // Time complexity: O(sqrt(n))
  // Space complexity: O(1)
  public static boolean isPrime(int n) {
    boolean isPrime = true;
    for(int i = 2; Math.sqrt(n) > i && isPrime; i++) {
      if(n % i == 0) isPrime = false;
    }
    return isPrime;
  }
  public static void main(String[] args) {
    System.out.println(isPrime(2) == true);
    System.out.println(isPrime(5) == true);
    System.out.println(isPrime(7) == true);
    System.out.println(isPrime(12) == false);
    System.out.println(isPrime(20) == false);
  }
}