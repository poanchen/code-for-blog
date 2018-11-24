public class logarithmicTime {
  
  // Time complexity: O(log(n))
  // Space complexity: O(1)
  public static int binarySearch(int [] arr, int target) {
    int low = 0, high = arr.length - 1;
    while(low <= high) {
      int mid = low + ((high - low) / 2);
      if(arr[mid] == target) return mid;
      if(arr[mid] < target) low = mid + 1;
      else high = mid - 1;
    }
    return -(low + 1);
  }
  public static void main(String[] args) {
    int [] arr = new int[]{2, 3, 5, 7, 9, 19, 25};
    System.out.println(binarySearch(arr, 2) == 0); // true
    System.out.println(binarySearch(arr, 19) == 5); // true
    System.out.println(binarySearch(arr, 1) == -1); // true
    System.out.println(binarySearch(arr, 20) == -7); // true
    System.out.println(binarySearch(arr, 18) == -6); // true
  }
}