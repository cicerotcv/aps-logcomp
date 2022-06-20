string concat(void a, void b) {
  return(a $ b);
}

integer main() {
  integer a, b;

  a = 10; # assignment
  b = 20;

  stdout(concat("a: ", a));
  stdout(concat("b: ", b));

  return(0);
}