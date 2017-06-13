function mutation(originalArray) {
  // directly mutating/modifying the original array
  originalArray[0] = "new value";
  return originalArray;
}

var array = ["some value", "another value"];
alert("Return from mutation " + mutation(array));
alert("Array: " + array + " (original array has been altered).");