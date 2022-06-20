void main() {
  integer b, c;

  b = 20;
  c = stdin();

  stdout("Test Comparisons");
  stdout("b: " $b);
  stdout("c: " $c);
  stdout("");

  if (b == c) {
    stdout("b == c");
  } else {
    stdout("b != c");

    if (b > c) {
      stdout("b > c");
    } else {
      stdout("b < c");
    }
  }
}