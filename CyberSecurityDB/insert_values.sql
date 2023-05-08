INSERT INTO employees (id, name, department) VALUES
(1, 'Alice', 'HR'),
(2, 'Bob', 'IT'),
(3, 'Carol', 'Finance');

INSERT INTO access_logs (id, employee_id, access_time, resource) VALUES
(1, 1, '2023-05-08 10:00:00', 'employee_records'),
(2, 2, '2023-05-08 11:00:00', 'network_devices'),
(3, 3, '2023-05-08 12:00:00', 'financial_reports'),
(4, 2, '2023-05-08 13:00:00', 'employee_records');

INSERT INTO file_modifications (id, employee_id, modification_time, file_name) VALUES
(1, 1, '2023-05-08 10:30:00', 'employee_records.docx'),
(2, 3, '2023-05-08 12:30:00', 'financial_reports.xlsx'),
(3, 2, '2023-05-08 13:30:00', 'employee_records.docx');