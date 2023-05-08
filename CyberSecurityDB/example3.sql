SELECT e.name, e.department, fm.file_name
FROM employees e
JOIN file_modifications fm ON e.id = fm.employee_id
LEFT JOIN access_logs al ON e.id = al.employee_id AND al.resource || '.docx' = fm.file_name
WHERE al.id IS NULL;