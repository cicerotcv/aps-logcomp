integer sum(integer a, integer b) {
    return(a + b);
}

integer max(integer a, integer b) {
  if (a > b) {
    return(a);
  }
  return(b);
}

string concat(void a, void b) {
  return(a$b);
}

integer main() {
  # single line comment
  /*
    Block comment
    -- accept multiline
  */
  integer a, b; # declaration
  a = 10; # assignment
  b = 20;

  stdout("Before Swap:");

  stdout("a: " $a);
  stdout("b: " $b);

  # this piece of code is expected to swap the variables 'a' and 'b'

  a = a * b;
  b = a / b; # a old value
  a = a / b; # b old value

  stdout("");
  stdout("After Swap:");

  stdout(concat("a: ", a));
  stdout(concat("b: ", b));

  return(0);
}