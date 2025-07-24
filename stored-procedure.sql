Select * from Employee where id=6

--------------------------------------------------------------------

--Stored Procedure without parameter

Create Procedure usp_GetAllEmployee
as
Begin
Select * from Employees  --table name employee
End

Alter Procedure usp_GetAllEmployee
as
Begin
Select * from Employee
End

--to execute
Execute usp_GetAllEmployee
exec usp_GetAllEmployee
usp_GetAllEmployee

-------------------------------------------------------------------

--Stored Procedure Selecting Specific Columns (No Parameters)

Create PROC usp_GetEmployeeInfo
as
begin
select id,name,dept from Employee1
end

usp_GetEmployeeInfo    --To run it

sp_helptext usp_GetEmployeeInfo    --To view the procedure code

Alter PROC usp_GetEmployeeInfo    --Altering already created procedure
as
begin
Select Name, dept from Employee1
end

Drop PROC usp_GetEmployeeInfo    --to delete procedure
---------------------------------------------------------------------
usp_Getallemployee
---------------------------------------------------------------------

--Create stored procedure using Single input parameter

Create PROC usp_GetEmployeeByDepartment
(@dept varchar(20))
as
begin
select * from Employee1 where dept=@dept
end

exec usp_GetEmployeeByDepartment 'HR'

-------------------------------------------------------------------

CREATE TABLE Employee2 (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    dept INT,
    salary DECIMAL(10, 2),
    gender VARCHAR(10)
);

INSERT INTO Employee2 (id, name, dept, salary, gender) VALUES
(1, 'Alice', 1, 50000, 'Female'),
(2, 'Bob', 2, 60000, 'Male'),
(3, 'Carol', 1, 55000, 'Female'),
(4, 'David', 2, 65000, 'Male'),
(5, 'Eve', 3, 70000, 'Female'),
(6, 'Frank', 2, 62000, 'Male');

select * from Employee2

--------------------------------------------------------------------

---Create another table called employee2 with gender

--Create stored procedure using Multiple input parameter

CREATE PROCEDURE usp_GetEmployeeByGenderAndDepartment
    @gender VARCHAR(10),
    @dept INT
AS
BEGIN
    SELECT * FROM Employee2
    WHERE gender = @gender AND dept = @dept;
END;

usp_GetAllEmployees

exec usp_GetEmployeeByGenderAndDepartment 'Male',2

exec usp_GetEmployeeByGenderAndDepartment @dept=1,@gender='Female'    --using named parameters

---------------------------------------------

--Example of stored Procedure with output parameter

create PROC spGetSum
(
@num1 int,
@num2 int,
@sum int output)
as
begin
set @sum=@num1+@num2
end

declare @sumResult int  --cannot make sumResult as varchar in declare coz of storing int values in sumResult
exec spGetSum 10,20,@sumResult OUT
print 'Result:' + Cast(@sumResult as varchar(20))  --cast to varchar to combine text + number

---------------------------------------------------------------------

--Example Employees Count By Gender (using Output)

Create PROC spGetEmployeeCountByGender
(@gender varchar(10), @empcount int OUT)
as
begin
select @empcount=count(ID) from Employee2 where gender=@gender
end

declare @empcount int
exec spGetEmployeeCountByGender 'male',@empcount OUT
print @empcount

--------------------------------------------------------------------

--Creating Stored Procedure using RETURN (only integer allowed)

create Proc spGetEmployeeCountByGender1
(@gender varchar(10))
as 
begin
return (select count(Id) from Employee2 where gender=@gender) --return can be only used for integer values
end

declare @empcount int
exec @empcount=spGetEmployeeCountByGender1 'Female'
print @empcount

-----------------------------------------------

--Altering Stored Procedure using RETURN

alter Proc spGetEmployeeCountByGender1
(@gender varchar(10))
as 
begin
return (select count(Id) from Employee2 where gender=@gender) --return can be only used for integer values
end

declare @empcount int
exec @empcount=spGetEmployeeCountByGender1 'male'
print @empcount

-----------------------------------------------------

--Procedure Returning Grouped Count (Using group by)

Alter Proc spGetEmployeeCountByGender1
as
begin
select gender, count(Id) from employee2 group by gender
end

exec spGetEmployeeCountByGender1

---------------------------------------------------

--Procedure with Two Output Parameters (Female & Male Count)

Alter Proc spGetEmployeeCountByGender1
(@femaleCount int OUT, @maleCount int OUT)
as
begin
select @femaleCount=count(id) from Employee2 where Gender='female'
select @maleCount=count(id) from Employee2 where Gender='male'
end

declare @femaleCount int, @maleCount int
exec spGetEmployeeCountByGender1 @femaleCount OUT, @maleCount OUT
print 'Female:' +cast(@femaleCount as varchar(10))+ ' , Male:' +Cast(@maleCount as varchar(5))

select * from Employee2

-------------------------------------------------------------------

--Encryption

Alter Proc spGetEmployeeCountByGender1
(@femaleCount int OUT, @maleCount int OUT)
With ENCRYPTION
as
begin
select @femaleCount=count(id) from Employee2 where Gender='female'
select @maleCount=count(id) from Employee2 where Gender='male'
end

sp_helptext spGetEmployeeCountByGender1

---------------------------------------------------------------

--Recompile

Alter Proc spGetEmployeeCountByGender1
(@femaleCount int OUT, @maleCount int OUT)
With RECOMPILE
as
begin
select @femaleCount=count(id) from Employee2 where Gender='female'
select @maleCount=count(id) from Employee2 where Gender='male'
end

---------------------------------------------------------------

--Stored Procedure with default value

Alter PROC spGetEmployeeCountByGender
(@gender varchar(10)='male', @empcount int OUT)
as
begin
select @empcount=count(ID) from Employee2 where gender=@gender
end

declare @count int
exec spGetEmployeeCountByGender @empcount=@count OUT  --no gender is specified,so default 'male' is used
print @count

declare @count1 int
exec spGetEmployeeCountByGender @gender='female', @empcount=@count1 OUT
print @count1














