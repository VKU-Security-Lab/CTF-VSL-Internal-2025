#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int setup(int argc, const char **argv, const char **envp) {
    setvbuf(stderr, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    return setvbuf(stdin, 0, 2, 0);
}

int main(int argc, const char **argv, const char **envp) {
    char bof[42]; 

    setup(argc, argv, envp);
    puts("Hi, Welcome to the pwn challenge!");
    puts("This program is just a print function. Bye!");
    puts("But wait, I have a present for you!");
    printf("%p\n", &fgets);
    printf("Please give me your present: ");
    gets(bof);
    return 0;
}