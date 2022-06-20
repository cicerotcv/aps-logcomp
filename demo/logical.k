integer log_and(integer a, integer b) {
  return (a and b);
}

integer log_or(integer a, integer b) {
  return (a or b);
}

integer log_not(integer a) {
  return (not a);
}

void main() {
  integer a, b;

  a = 1;
  b = 0;

  stdout("Logical Operations");

  stdout("a and b: " $log_and(a, b));
  stdout("a or b: " $log_or(a, b));
  stdout("not a: " $log_not(a));
  stdout("not b: " $(not b));
}