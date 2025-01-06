#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <time.h>
#include <stdbool.h>

#define MAX_SIZE 100

int canaryCheck;

int setup()
{
    int seed = time(NULL);
    srand(seed);
    canaryCheck = rand();
    return canaryCheck;
}

void execute_command(char *command)
{
    system(command);
}

bool check_canary(int canary)
{
    return canary == canaryCheck;
}

int main()
{
    // Random canary
    int canary = setup();
    int students[10];
    int canary1 = 9876543;
    int check[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int id;
    // Print canary
    printf("Canary: %d\n", canary);
    while (1)
    {
        printf("Enter student ID: ");
        scanf("%d", &id);
        if (id == 1337)
        {
            break;
        }
        printf("Value: ");
        printf("%d\n", students[id]);
    }

    return 0;
}