integer max(integer a, integer b) {
  if (a > b) {
    return(a);
  }
  return(b);
}

integer main() {
  integer a, b;
  a = 10;
  b = 20;

  stdout("a: " $a);
  stdout("b: " $b);

  stdout("max(a, b): " $max(a, b));

  return(0);
}