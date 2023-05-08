CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50)
);

CREATE TABLE access_logs (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    access_time DATETIME,
    resource VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE TABLE file_modifications (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    modification_time DATETIME,
    file_name VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);