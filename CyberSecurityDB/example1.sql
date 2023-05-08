SELECT e.name, e.department, al.resource, al.access_time, fm.modification_time
FROM employees e
JOIN access_logs al ON e.id = al.employee_id
JOIN file_modifications fm ON e.id = fm.employee_id
WHERE CONCAT(al.resource, '.docx') = fm.file_name
AND UNIX_TIMESTAMP(fm.modification_time) - UNIX_TIMESTAMP(al.access_time) <= 3600
LIMIT 1000;