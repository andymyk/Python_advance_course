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
    print('Error while creating the connection', err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        sql_insert_emp = """INSERT INTO EMPLOYEES VALUES (:1,:2,:3,:4)"""
        data_employees = [(1, 'Петров Петр Петрович', 'ШеФ', 101), (2, 'Андрей Андреев Андреевич', 'Шофер', 105),
                          (3, 'Вася Васин Васильевич', 'Работник', 103), (4, 'Иван Иванов Иванович', 'Работник', 103),
                          (5, 'Леонид Яковлев Ильич', 'Охранник', 105), (6, 'Ирина Кукшу Викторовна', 'Секретарь', 103)]
        sql_insert_dep = """INSERT INTO DEPARTMENTS VALUES (:1,:2)"""
        data_dep = [(101, 'Главный офис'),
                    (105, 'Логистика'),
                    (103, 'Работники')]
        sql_insert_orders = """INSERT INTO ORDERS VALUES (:1,:2,:3,:4,:5,:6,:7,:8)"""
        data_orders = [(10001, '01-AUG-21', '03-AUG-21', 'плановое обслуживание', 'описание', 'In process', 123456, 1),
                       (10002, '29-JUL-21', '01-AUG-21', 'инсталяция', 'описание', 'Closed', 123222, 4),
                       (10003, '29-JUL-21', '02-AUG-21', 'инсталяция', 'описание', 'Closed', 333221, 4),
                       (10004, '30-JUL-21', '02-AUG-21', 'консультация', 'описание', 'Closed', 12321, 3),
                       (10005, '02-AUG-21', '03-AUG-21', 'плановое обслуживание', 'описание', 'In process', 111122, 3),
                       (10006, '01-AUG-21', '03-AUG-21', 'плановое обслуживание', 'описание', 'In process', 333121, 3)]
        cur.executemany(sql_insert_emp, data_employees)
        cur.executemany(sql_insert_dep, data_dep)
        cur.executemany(sql_insert_orders, data_orders)
    except Exception as err:
        print('Error while inserting the data', err)
    else:
        print('Insert completed')
        conn.commit()
finally:
    cur.close()
    conn.close()
