CREATE TABLE Department
(
ID INT PRIMARY KEY,
Name VARCHAR(50)
)
GO
-- Populate the Department Table with test data
INSERT INTO Department VALUES(1, 'IT')
INSERT INTO Department VALUES(2, 'HR')
INSERT INTO Department VALUES(3, 'Sales')
-- Create Employee Table
CREATE TABLE Employee
(
ID INT PRIMARY KEY,
Name VARCHAR(50),
Gender VARCHAR(50),
DOB DATETIME,
DeptID INT
)
GO
-- Populate the Employee Table with test data
INSERT INTO Employee VALUES(1, 'Pranaya', 'Male','1996-02-29 10:53:27.060', 1)
INSERT INTO Employee VALUES(2, 'Priyanka', 'Female','1995-05-25 10:53:27.060', 2)
INSERT INTO Employee VALUES(3, 'Anurag', 'Male','1995-04-19 10:53:27.060', 2)
INSERT INTO Employee VALUES(4, 'Preety', 'Female','1996-03-17 10:53:27.060', 3)
INSERT INTO Employee VALUES(5, 'Sambit', 'Male','1997-01-15 10:53:27.060', 1)
INSERT INTO Employee VALUES(6, 'Hina', 'Female','1995-07-12 10:53:27.060', 2)
GO

select * from dbo.Department

select * from dbo.Employee

-- Creating View
CREATE VIEW vwGetAllEmployees
AS 
SELECT * FROM Employee

-- View with specific columns
CREATE VIEW vwAllEmployees2 
AS 
SELECT ID, Name, Gender, DOB, DeptID 
FROM Employee

select * from vwAllEmployees2

---DML---
Insert into vwAllEmployees2 values(7,'Santhosh','M','1-2-2004',1)

Update vwAllEmployees2 SET Name='Santhosh M' where id=7

Delete from vwAllEmployees2 where id=1

--Complex View Example with Different table

Create View  vwAllEmployeesWithDepartment
as
Select e.id, e.Name, e.Gender, e.DOB, d.Name as DepartmentName
from Employee e
inner join Department d
on e.deptid=d.id

select * from vwAllEmployeesWithDepartment

--Cannot perform DML when view has multiple tables, throws error
--insert into vwAllEmployeesWithDepartment values(8,'Harry','M','2-2-24','Data')

--Complex View with Single table

Create View vwAllEmployeeCountByGender
as
Select Gender,Count(*) as TotalEmployee
from Employee Group by Gender

select * from vwAllEmployeeCountByGender

--Cannot perform DML when aggregate func, group by clause are used in the view
--insert into vwAllEmployeeCountByGender values ('others',3)

select * from Employee
select * from Department

create view vwHREmployees
as
select * from Employee where DeptId=2

select * from vwHREmployees

--while inserting dept_id have to be same as mentioned in view while creating it
insert into vwHREmployees values(11,'Ankita','F','2004-03-03',2)
INSERT INTO vwHREmployees VALUES (9, 'Ankita', 'F', '2004-03-03', 2);

alter view vwHREmployees
as 
select * from Employee where DeptId=2
with check option

sp_helptext vwHREmployees
sp_help Employee

--Creating View based on another view
Create View vwITEmployees
as
Select Id, Name, DOB, Gender,DeptId from
vwGetAllEmployees where DeptID=1

select * from vwITEmployees


-----------------------------------------------

CREATE TABLE Employee1 (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dept VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO Employee1 VALUES (1, 'John', 'HR', 50000.00),
(2, 'Alice', 'IT', 65000.00),
(3, 'Bob', 'Finance', 55000.00),
(4, 'Meena', 'IT', 70000.00),
(5, 'Ravi', 'HR', 48000.00);

INSERT INTO Employee1 VALUES (6, 'Priya', 'Finance', 60000.00),
(7, 'Karan', 'HR', 52000.00),
(8, 'Sneha', 'IT', 72000.00),
(9, 'Arjun', 'Finance', 58000.00),
(10, 'Divya', 'HR', 51000.00);

select * from Employee1

--CTE

WITH HighSalaryCTE AS (
    SELECT Id, Name, dept AS Department, Salary
    FROM Employee1
    WHERE Salary >= 50000
)
SELECT * FROM HighSalaryCTE;

select * from Employee1

select name,salary,e.dept,d.totalEmployees, d.TotalSalary,
d.MinSal,d.MaxSal,d.AvgSal
from Employee1 e
inner join
(select Dept,
count(*) as totalEmployees, 
sum(salary) as TotalSalary,
min(salary) as MinSal,
max(salary) as MaxSal,
avg(salary) as AvgSal
from Employee1
group by dept) d on d.dept=e.dept


--same result using Over Clause

select Name,Salary,Dept,
count(dept) OVER(Partition by dept) as deptTotals,
sum(salary) OVER(Partition by dept) as TotalSal,
min(salary) OVER(Partition by dept) as minSal,
max(salary) OVER(Partition by dept) as maxSal,
avg(salary) OVER(Partition by dept) as Avgsal
from Employee1

--It adds up the salaries of all people in the same department.
--Again, PARTITION BY dept keeps the sum limited to their department.
--Example: If IT department has salaries 65000 and 70000, each IT employee will see 135000 in TotalSal

SELECT Name,Dept, salary,
ROW_NUMBER() OVER(Partition By dept Order by Name)
as RowNumber from Employee1;

-------------------
--RANK()
select Name,dept,salary,
RANK() OVER(Partition by dept ORDER BY salary desc) as [RANK]
from Employee1

--DENSE_RANK()
select Name,dept,salary,
DENSE_RANK() OVER(Partition by dept ORDER BY salary desc) as [RANK]
from Employee1

WITH EmployeeCTE as(
select salary, RANK() OVER( Order by salary desc) as Rank_salary
from Employee1)
select top 1 salary from EmployeeCTE where Rank_salary=2

WITH EmployeeCTE as(
select salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS DenseRank_Salry
    FROM Employee1)
SELECT TOP 1 Salary FROM EmployeeCTE WHERE DenseRank_Salry = 2;

WITH EmployeeCTE AS (
    SELECT Salary, Dept,
           DENSE_RANK() OVER (PARTITION BY Dept ORDER BY Salary DESC) AS Salary_Rank
    FROM Employee1
)
SELECT TOP 1 Salary 
FROM EmployeeCTE 
WHERE Salary_Rank = 3 AND Dept= 'IT';





