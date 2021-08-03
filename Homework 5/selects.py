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
        sql = """SELECT * FROM EMPLOYEES"""
        cur.execute(sql)
        row = cur.fetchall()
        for index, i in enumerate(set(row)):
            print(index, i, end='\n')
    except Exception as err:
        print('Excption occured while fetching the records', err)
    else:
        print('Completed')
    finally:
        cur.close()
finally:
    conn.close()
