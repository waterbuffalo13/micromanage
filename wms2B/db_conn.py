import sqlite3

from wms2B.data.employee import Employee


class Database:

    def __init__(self, name):
        emp_1 = Employee('Jake', 'Williams', '80,000.00')
        emp_2 = Employee('Django', 'Henry', '68,000.00')

        self._conn = sqlite3.connect(name, check_same_thread=False)
        self._cursor = self._conn.cursor()

        self._cursor.execute("""CREATE TABLE employees (
                     first text,
                     last text,
                     pay real
             )""")
        self._cursor.execute("INSERT INTO employees VALUES (?, ? ,?)", (emp_1.first, emp_1.last, emp_1.pay))
        self._cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()