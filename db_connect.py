import pymssql


def init_db_connect(host, user, password, db_name):
    try:
        conn = pymssql.connect(host, user, password, db_name)
    except pymssql.InterfaceError:
        print('Failed to connect to database "{}"'.format(DB_NAME))
        sys.exit(1)
    else:
        return conn


def add_rows_to_sql(sql_query, sql_value, db_connect):
    with db_connect:
        cursor = conn.cursor()
        cursor.executemany(sql_query, sql_value)
        conn.commit()


def add_news_to_sql(add_tuple):
    sql_query = (
        """
            INSERT INTO table_name (cell1, cell2, cell3, cell4)
            VALUES (%d, %s, %s, %s)
        """
    )
    add_rows_to_dbl(sql_query, add_tuple)
