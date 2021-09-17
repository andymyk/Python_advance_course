from config import host, user, password, db_name
import psycopg2


class DBClient:
    CHECK_ACTIVE = """SELECT COUNT(status) FROM orders WHERE status = 'Active'"""
    CHECK_PERSONAL = """SELECT personal_data, department_name FROM employees e LEFT JOIN departments d"""
    CHECK_DATA = """SELECT * FROM orders WHERE created_dt = '2021-09-07'"""
    CHECK_ID_ORDERS = """SELECT order_id, personal_data FROM orders o
LEFT JOIN employees e ON(o.creator_id = e.employee_id)"""


    def __init__(self):
        self.connect = None

    def setup(self):
        self.connect = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

    def check_status_a(self):
        with self.connect.cursor() as cursor:
            cursor.execute(self.CHECK_ACTIVE)
            self.connect.commit()

    def check_p(self):
        with self.connect.cursor() as cursor:
            cursor.execute(self.CHECK_PERSONAL)
            self.connect.commit()

    def check_d(self):
        with self.connect.cursor() as cursor:
            cursor.execute(self.CHECK_DATA)
            self.connect.commit()

    def check_id_o(self):
        with self.connect.cursor() as cursor:
            cursor.execute(self.CHECK_ID_ORDERS)
            self.connect.commit()