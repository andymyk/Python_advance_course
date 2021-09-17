import psycopg2

CREATE = """CREATE TABLE SUBSCRIBERS(
username VARCHAR(30) NOT NULL,
is_subscribed VARCHAR(30) NOT NULL
)"""

INSERT = """INSERT INTO SUBSCRIBERS VALUES('Andy','True');
INSERT INTO SUBSCRIBERS VALUES('Peter','True');
INSERT INTO SUBSCRIBERS VALUES('John','False');
INSERT INTO SUBSCRIBERS VALUES('George','True');
INSERT INTO SUBSCRIBERS VALUES('Michael','False');
INSERT INTO SUBSCRIBERS VALUES('Oliver','True');
INSERT INTO SUBSCRIBERS VALUES('Dorothea','False');"""

CHECK_ACTIVE = """SELECT * FROM subscribers where is_subscribed ='True';"""
CHECK_FALSE = """SELECT * FROM subscribers where is_subscribed ='True';"""


conn = psycopg2.connect(
    host='127.0.0.1',
    user='postgres',
    password='123',
    database='data'
)
# with conn.cursor() as cursor:
#     cursor.execute(CREATE)
#     conn.commit()
# with conn.cursor() as cursor:
#     cursor.execute(INSERT)
#     conn.commit()
# with conn.cursor() as cursor:
#     cursor.execute(CHECK_ACTIVE)
#     row = cursor.fetchall()
#     for i in row:
#         if i[1] == 'True':
#             cursor.execute(f"""UPDATE subscribers SET is_subscribed = 'False' where username = '{i[0]}';""")
#             conn.commit()
# with conn.cursor() as cursor:
#     cursor.execute(CHECK_FALSE)
#     row = cursor.fetchall()
#     for i in row:
#         if i[1] == 'True':
#             cursor.execute(f"""UPDATE subscribers SET is_subscribed = 'False' where username = '{i[0]}';""")
#             conn.commit()
