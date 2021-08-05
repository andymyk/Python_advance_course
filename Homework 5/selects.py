import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\carje\Downloads\instantclient")
hostname = 'localhost'
port = 1521
SID = 'xe'
username = 'demo'
password = 'demo'

dsn_tns = cx_Oracle.makedsn(hostname, port, SID)

try:
    conn = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
except Exception as err:
    print('Exception occured while trying to create a connection', err)
else:
    try:
        cur = conn.cursor()
        sel_1 = """SELECT * FROM ORDERS WHERE STATUS = 'In process' AND CREATOR_ID = 3
AND CREATED_DT = '01-AUG-21' """
        sel_2 = """SELECT COUNT(status) FROM orders WHERE status = 'Closed'"""
        sel_3 = """SELECT FIO, department_name FROM employees e LEFT JOIN departments d
ON (d.department_id = e.department_id)"""
        sel_4 = """SELECT order_id, fio FROM orders o
        LEFT JOIN employees e ON(o.creator_id = e.employee_id)"""
        cur.executemany(sel_1,sel_2,sel_3,sel_4)
        rows = cur.fetchall()
        print(rows)
    except Exception as err:
        print('Excption occured while fetching the records', err)
    else:
        print('Completed')
    finally:
        cur.close()
finally:
    conn.close()
