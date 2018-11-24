public class exponentiationTime {
  
  // Time complexity: O(4^n)
  // Space complexity: O(1)
  public static void getMaxAnswer(double res, int [] arr, int index) {
    if(index == arr.length) {
      System.out.println(res);
    } else {
      getMaxAnswer(res + arr[index], arr, index + 1);
      getMaxAnswer(res - arr[index], arr, index + 1);
      getMaxAnswer(res * arr[index], arr, index + 1);
      getMaxAnswer(res / arr[index], arr, index + 1);
    }
  }
  public static void main(String[] args) {
    int [] arr = new int[]{1, 12, 3};
    getMaxAnswer(arr[0] * 1.0, arr, 1);
  }
}