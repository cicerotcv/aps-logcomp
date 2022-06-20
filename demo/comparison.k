void main() {
  integer a, b, c;

  b = 10;
  c = 10;

  stdout("b: "$b);
  stdout("c: "$c);

  stdout("");

  stdout("b > c: " $(b > c));
  stdout("b >= c: " $(b >= c));
  stdout("b < c: " $(b < c));
  stdout("b <= c: " $(b <= c));
  stdout("b == c: " $(b == c));
  stdout("b != c: " $(b != c));
}