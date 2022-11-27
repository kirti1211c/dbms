from flask_mysqldb import MySQL



# Not thread-safe
class _Mysql:
    def __init__(self, mysql_connection):
        self._mysql = mysql_connection
    
    def __enter__(self):
        self._cursor = self._mysql.connection.cursor()
        return self._cursor
        
    def __exit__(self, exc_type, exc_value, tb):
        self._cursor.close()
        self._cursor = None
        self._mysql.connection.commit()

        if exc_type is not None:
            return False 

        return True

class _DB:
    def __init__(self):
        self._mysql = None
        
    
    def _set_mysql_connection(self, app):
        self._mysql = _Mysql(MySQL(app))

    def cursor(self):
        if (not self._mysql):
            raise RuntimeError("DB was not initalised successfully...")
        
        
        
        return self._mysql

db = _DB()

__all__ = ["db"]