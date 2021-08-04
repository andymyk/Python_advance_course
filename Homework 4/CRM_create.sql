CREATE TABLE ORDERS(
order_id INTEGER,
created_dt DATE DEFAULT SYSDATE,
updated_dt DATE,
order_type VARCHAR2(25),
"DESCRIPTION" VARCHAR2(25),
status VARCHAR2(10),
serial_no INTEGER,
creator_id INTEGER
);

CREATE TABLE EMPLOYEES2(
employee_id INTEGER,
fio VARCHAR2(25),
position VARCHAR2(20),
department_id INTEGER
);


CREATE TABLE DEPARTMENTS(
department_id INTEGER,
department_name VARCHAR2(20)
);