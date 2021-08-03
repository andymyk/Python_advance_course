import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\carje\Downloads\instantclient")
hostname = 'localhost'
port = 1521
SID = 'xe'
username = 'demo'
password = 'demo'

dsn_tns = cx_Oracle.makedsn(hostname, port, SID)
conn = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)

cur = conn.cursor()

sql_create = """
CREATE TABLE ORDERS(
order_id INTEGER,
created_dt DATE DEFAULT SYSDATE,
updated_dt DATE,
order_type VARCHAR2(55) ,
"DESCRIPTION" VARCHAR2(55),
status VARCHAR2(50),
serial_no INTEGER,
creator_id INTEGER
)
"""
sql_cr = """
CREATE TABLE EMPLOYEES(
employee_id INTEGER,
fio VARCHAR2(55),
position VARCHAR2(50),
department_id INTEGER
)"""

sql_cre = """
CREATE TABLE DEPARTMENTS(
department_id INTEGER,
department_name VARCHAR2(50))
"""

cur.execute(sql_create)
cur.execute(sql_cr)
cur.execute(sql_cre)
print('Tables created.')

cur.close()
conn.close()
