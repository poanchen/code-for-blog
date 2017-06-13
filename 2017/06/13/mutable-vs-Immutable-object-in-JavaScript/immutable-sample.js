function immutable(originalArray) {
  // Instead of mutating/modifying the original array,
  // we first make a copy of the original array
  // In this way, the original array stay unchanged.
  var newArray = [...originalArray];
  newArray[0] = "new value";
  return newArray;
}

var array = ["some value", "another value"];
alert("Return from immutable " + immutable(array));
alert("Array: " + array + " (original array stay unchanged).");