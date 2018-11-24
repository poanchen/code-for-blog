public class threeLinearTime {
  
  // Time complexity: O(n)
  // Space complexity: O(1)
  public static void printArray(int [] arr) {
    for(int i = 0; i < arr.length; i++) {
      System.out.println(arr[i]);
    }
  }
  public static void main(String[] args) {
    int [] arr = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    printArray(arr);
    printArray(arr);
    printArray(arr);
  }
}