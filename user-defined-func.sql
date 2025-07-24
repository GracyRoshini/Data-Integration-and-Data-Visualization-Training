--User Defined Function

CREATE TABLE Employee3 (
    Id INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Dob DATE,
    Dept INT
);


CREATE TABLE Dept (
    Id INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

INSERT INTO Employee3 (Id, Name, Gender, Dob, Dept)
VALUES 
(1, 'Alice', 'Female', '1998-04-12', 1),
(2, 'Bob', 'Male', '1995-07-19', 2),
(3, 'Catherine', 'Female', '1992-11-05', 3),
(4, 'David', 'Male', '1990-06-23', 2),
(5, 'Eva', 'Female', '1996-09-10', 1),
(6, 'Frank', 'Male', '1989-12-30', 3);

INSERT INTO Dept (Id, DeptName)
VALUES 
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

----Scalar Values Function
--Example 1:
Create Function SVF1(@num INT)
RETURNS INT
AS
BEGIN
RETURN @num*@num*@num
END

SELECT dbo.SVF1(3)

Select * from Employee2
--------------------------------
--example2 2:
Create Function FN_GetEmployeeByDept
(@dept int)
RETURNS TABLE
AS
RETURN (SELECT id, name, gender,dept from Employee2 where dept=@dept)

select * from dbo.FN_GetEmployeeByDept(2)

-----------------------------------------------------------

--Inline Table-Valued Function
Create Function FN_GetEmployeeByGender
(
@gender varchar(20)
)
RETURNS TABLE
AS
RETURN (
    SELECT * from Employee3 where Gender=@gender
    )

select * from dbo.FN_GetEmployeeByGender('Male')

--Using in a JOIN

select Name,gender,dob,dept 
from FN_GetEmployeeByGender('Male') emp
Inner Join dept d 
on d.id=emp.dept

--Inline TVF with Join Logic Inside
--Example for return data from Multiple table using table values func

create Function FN_EmployeesByGender
(@gender varchar(50))
RETURNS TABLE
as
Return (
    Select Name, gender, dob,dept 
    from Employee3 emp
    Inner join dept d 
    on d.id=emp.dept
    where gender=@gender
    )

select * from dbo.FN_EmployeesByGender('Female')

--------------------------------------------------------------------
--Example for Multi-Statement table values func

--eg:1
Create Function FN_MultiStmt()
returns @MyTable Table (Id int, Name varchar(40))  --mytable is temporary table 
as
BEGIN
Insert into @MyTable 
Select Id, Name from Employee3
RETURN 
END

Select * from FN_MultiStmt()
-------------------------------------

--eg:2
CREATE FUNCTION FN_EmployeesAboveAge
(@minAge INT)
RETURNS @Result TABLE (
    Id INT,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    DeptName VARCHAR(50)
)
AS
BEGIN
    -- Insert employees above a certain age into the return table
    INSERT INTO @Result
    SELECT 
        e.Id,
        e.Name,
        e.Gender,
        DATEDIFF(YEAR, e.dob, GETDATE()) AS Age,  -- Calculates age
        d.deptName
    FROM Employee3 e
    INNER JOIN dept d ON d.id = e.dept
    WHERE DATEDIFF(YEAR, e.dob, GETDATE()) > @minAge
    RETURN
END

SELECT * FROM FN_EmployeesAboveAge(25)

----------------------------------------------------------------------






















