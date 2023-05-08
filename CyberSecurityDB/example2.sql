SELECT e.name, e.department, al.resource
FROM employees e
JOIN access_logs al ON e.id = al.employee_id
WHERE (
    (e.department = 'HR' AND al.resource != 'employee_records') OR
    (e.department = 'IT' AND al.resource != 'network_devices') OR
    (e.department = 'Finance' AND al.resource != 'financial_reports')
);