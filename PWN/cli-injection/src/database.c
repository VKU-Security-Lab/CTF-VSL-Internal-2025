#include "database.h"
#include <stdio.h>

MYSQL *db_connect(const char *server, const char *user, const char *password, const char *database)
{
    MYSQL *conn = mysql_init(NULL);
    if (!mysql_real_connect(conn, server, user, password, database, 3306, NULL, 0))
    {
        fprintf(stderr, "Error: %s\n", mysql_error(conn));
        return NULL;
    }
    return conn;
}

MYSQL_RES *db_query(MYSQL *conn, const char *query)
{
    if (mysql_query(conn, query))
    {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return NULL;
    }
    return mysql_use_result(conn);
}

void db_close(MYSQL *conn)
{
    if (conn != NULL)
    {
        mysql_close(conn);
    }
}
