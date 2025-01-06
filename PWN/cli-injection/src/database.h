#ifndef DATABASE_H
#define DATABASE_H

#include <mysql/mysql.h>

MYSQL *db_connect(const char *server, const char *user, const char *password, const char *database);
void db_close(MYSQL *conn);
MYSQL_RES *db_query(MYSQL *conn, const char *query);

void db_close(MYSQL *conn);

#endif 
