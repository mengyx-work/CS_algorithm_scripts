ELECT employee.Name AS Employee
FROM Employee employee
INNER JOIN Employee manager ON manager.id = employee.ManagerId
WHERE employee.ManagerId  IS NOT NULL AND employee.Salary > manager.Salary

