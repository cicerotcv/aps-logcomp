void main() {
  integer a, b;

  a = 1;
  b = 5;

  while (a <= b) {
    stdout("a <= b: " $"a: " $a $" b: " $b);
    a = a + 1;
  }

  stdout("a > b: " $"a: "$a $" b: "$b);
}