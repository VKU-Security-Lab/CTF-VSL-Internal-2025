#include<stdio.h>

char *secret = "How did you find me? Here is the flag: VSL{%s}";

void hacked() {
    printf("Hacked!\n");
    printf(secret, "4a7b886cf1c4ab93e740c5ef935749ce");
}

int main() {
    int i;
    for(i = 0; i < 10; i++) {
        printf("Hello, World!\n");
    }
    hacked();
    return 0;
}