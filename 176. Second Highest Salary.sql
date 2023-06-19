SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
LEFT JOIN (
    SELECT MAX(salary) AS salary1
    FROM Employee
) AS tbl1
ON (salary = salary1)
WHERE salary1 IS NULL


