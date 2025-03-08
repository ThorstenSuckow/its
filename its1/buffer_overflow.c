#include <stdio.h>
#include <string.h>
#include <malloc.h>

void main() {

    int ok = 0;
    char target[4] = "olds";  

    printf("ok address: %d\n", &ok);
    printf("ok contents: %d\n", ok);
    printf("sizeof 'target': %d\n", (sizeof(target) * sizeof(char)));
        
    
    strcpy(target, "Hello");

    if (ok) {
        printf("sizeof 'Hello': %d\n", sizeof("Hello"));
        
        printf("ok address: %d\n", &ok);
        char t = (char)ok;
        printf("ok contents (dec): %d\n", ok);
        printf("ok contents (char): %c\n", t);

        printf("This message should not appear - strcpy caused an overflow!");
    }

}