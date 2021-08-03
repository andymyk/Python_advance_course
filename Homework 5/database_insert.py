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