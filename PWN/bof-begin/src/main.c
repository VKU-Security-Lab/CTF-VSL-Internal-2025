#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int ROOT_ID = 1337;
int GUEST_ID = 0;

struct user {
    char username[12];
    char password[12];
    int role;
};

void win() {
    printf("You win!\n");
    fflush(stdout);
    system("/bin/sh");
}

int main(int argc, char *argv[]) {
    struct user u;
    u.role = GUEST_ID;
    printf("Enter username: ");
    fflush(stdout);
    gets(u.username);
    printf("Enter password: ");
    fflush(stdout);
    gets(u.password);

    if (!strcmp(u.username, "admin")) {
        if (u.role == ROOT_ID) 
        {
            printf("Welcome, root!\n");
            fflush(stdout);
            system("/bin/sh");
        } 
        else if (u.role == GUEST_ID) {
            printf("Welcome, guest!\n");
            fflush(stdout);
        } else
        {
            printf("Nice try, but you are not root!\n");
            fflush(stdout);
        }
    } else {
        printf("Welcome, %s!\n", u.username);
        fflush(stdout);
    }
}