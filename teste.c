integer max(integer a, integer b) {
    if (a > b) {
        return(a);
    }
    return(b);
}

integer soma(integer a, integer b) {
    return (a + b);
}

integer swap(integer a, integer b) {
    a = (a + b + 1) / 2;
    b = (a - b + 1) / 2;

}

void main(){
    # this is a line comment (just like we use in python)
    # I've called it "hash comment"
    integer a, b; # these are variable declarations
    
    /*
    	This is a block comment
        with as many lines as you want 
    */
    
    a = 3; # assignment
    b = 1; # assignment

    printf(max(a, b));
    printf(soma(a, b));

    # swap a and b
    
    printf("Before swap: ");
    printf(a);
    printf(b);

    a = a * b;
    b = a / b;
    a = a / b;

    printf("After swap: ");
    printf(a);
    printf(b);

}