#include "database.h"
#include <stdio.h>
#include <stdlib.h>

int check_login = 0;

void setup()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}


int login_query(MYSQL *conn, const char *username, const char *password);
void register_user(MYSQL *conn);
int register_query(MYSQL *conn, const char *username, const char *password, const char *fullname);
// void view_profile(MYSQL *conn);
// void change_password(MYSQL *conn);
int after_login(MYSQL *conn);

void menu_1()
{
    printf("1. Login\n");
    printf("2. Register\n");
    printf("3. Exit\n");
    printf("Your choice: ");
}

void menu_2()
{
    printf("1. View profile\n");
    printf("2. Change password\n");
    printf("3. Logout\n");
    printf("Your choice: ");
}

void login(MYSQL *conn)
{
    char username[137];
    char password[137];
    printf("Username: ");
    scanf("%s", username);
    printf("Password: ");
    scanf("%s", password);

    if (login_query(conn, username, password) > 0)
    {
        printf("Login successful!\n");
        check_login = 1;
    }
    else
    {
        printf("Login failed!\n");
    }
}

int login_query(MYSQL *conn, const char *username, const char *password)
{
    char query[1337];
    sprintf(query, "SELECT * FROM users WHERE username='%s' AND password='%s'", username, password);
    MYSQL_RES *res = db_query(conn, query);
    if (res == NULL)
    {
        return -1; 
    }

    int num_rows = mysql_num_rows(res);
    mysql_free_result(res);

    return num_rows;
}

void register_user(MYSQL *conn)
{
    char username[137];
    char password[137];
    char fullname[137];
    printf("Username: ");
    scanf("%s", username);
    printf("Password: ");
    scanf("%s", password);
    printf("Fullname: ");
    scanf("%s", fullname);

    if (register_query(conn, username, password, fullname) > 0)
    {
        printf("Register successful!\n");
    }
    else
    {
        printf("Register failed!\n");
    }
}

int register_query(MYSQL *conn, const char *username, const char *password, const char *fullname)
{
    char query[1337];
    sprintf(query, "INSERT INTO users (username, password, fullname) VALUES ('%s', '%s', '%s')", username, password, fullname);
    if (db_query(conn, query) == NULL)
    {
        return -1;
    }

    return 1;
}

int after_login(MYSQL *conn)
{
    int choice;
    // while (login == 1)
    // {
    //     menu_2();
    //     scanf("%d", &choice);
    //     switch (choice)
    //     {
    //         case 1:
    //         {
    //             view_profile(conn);
    //             break;
    //         }
    //         case 2:
    //         {
    //             change_password(conn);
    //             break;
    //         }
    //         case 3:
    //         {
    //             login = 0;
    //             break;
    //         }
    //         default:
    //             printf("Invalid choice!\n");
    //             break;
    //     }
    // }
    return 0;
}

int main()
{
    setup();
    const char *server = getenv("DB_SERVER") ? getenv("DB_SERVER") : "localhost";
    const char *user = getenv("DB_USER") ? getenv("DB_USER") : "root";
    const char *password = getenv("DB_PASSWORD") ? getenv("DB_PASSWORD") : "";
    const char *database = getenv("DB_NAME") ? getenv("DB_NAME") : "test";
    MYSQL *conn = db_connect(server, user, password, database);
    if (conn == NULL)
        return 1; 

    menu_1();
    int choice;
    while (login == 0)
    {
        scanf("%d", &choice);
        switch (choice)
        {
            case 1:
            {
                login(conn);
                break;
            }
            case 2:
            {
                register_user(conn);
                break;
            }
            case 3:
            {
                db_close(conn);
                printf("Goodbye!\n");
                return 0;
            }
            default:
                printf("Invalid choice!\n");
                break;
        }
    }

    if (check_login == 1)
    {
        after_login(conn);
    }
    return 0;
}
