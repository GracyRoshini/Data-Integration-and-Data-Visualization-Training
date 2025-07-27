--Creating table tblEmployee
CREATE TABLE tblEmployee
(
  Id int Primary Key,
  Name nvarchar(30),
  Salary int,
  Gender nvarchar(10),
  DepartmentId int
)


--Insert data into tblEmployee table
Insert into tblEmployee values (1,'John', 5000, 'Male', 3)
Insert into tblEmployee values (2,'Mike', 3400, 'Male', 2)
Insert into tblEmployee values (3,'Pam', 6000, 'Female', 1)


--Creating an audit table to track changes
CREATE TABLE tblEmployeeAudit
(
  Id int identity(1,1) primary key,  --coln names
  AuditData nvarchar(1000)
)


--Viewing tables
SELECT * FROM tblEmployee
SELECT * from tblEmployeeAudit  --initially empty


/*-- INSTEAD OF INSERT trigger to restrict insertions
CREATE TRIGGER trg_insteadofInsert_Employee
ON tblEmployee
INSTEAD OF INSERT
AS
BEGIN
    PRINT 'Insertion denied'
    ROLLBACK  --ensures any transaction in progress is reversed. Cancels the insert operation explicitly
END

Insert into tblEmployee values (8,'Tan1', 2300, 'Female', 3) --(Error msg: Insertion denied. The transaction ended in the trigger. The batch has been aborted)
*/

--DROP TRIGGER trg_insteadofInsert_Employee;  --need to drop instead of trigeer to run the for trigger again

--Creating trigger for insert actions
Alter TRIGGER tr_tblEMployee_ForInsert
ON tblEmployee
FOR INSERT
AS
BEGIN
 Declare @Id int
 Select @Id = Id from inserted  --inserted is a table that temp stores values that are inserted
 
 insert into tblEmployeeAudit 
 values('New employee with Id  = ' + Cast(@Id as nvarchar(5)) + ' is added at ' + cast(Getdate() as nvarchar(20)))
END


Insert into tblEmployee values (10,'Tan1', 2300, 'Female', 3)


--Trigger for UPDATE audit  -- while updating new value is inserted and old value is deleted
--CREATE 
Alter trigger tr_tblEmployee_ForUpdate
on tblEmployee
for Update
as
Begin
      -- Declare variables to hold old and new updated data
      Declare @Id int
      Declare @OldName nvarchar(20), @NewName nvarchar(20)
      Declare @OldSalary int, @NewSalary int
      Declare @OldGender nvarchar(20), @NewGender nvarchar(20)
      Declare @OldDeptId int, @NewDeptId int
     
      -- Variable to build the audit string
      Declare @AuditString nvarchar(1000)  --output string
      
      -- Load the updated records into temporary table
      Select *
      into #TempTable  --default temp table that is cloned, we cannot view other data inside this table
      from inserted  --temp table w inserted values
     
      -- Loop thru the records in temp table
      While(Exists(Select Id from #TempTable))
      Begin
            --Initialize the audit string to empty string
            Set @AuditString = ''
           
            -- Select first row data from temp table
            Select Top 1 @Id = Id, @NewName = Name, 
            @NewGender = Gender, @NewSalary = Salary,
            @NewDeptId = DepartmentId
            from #TempTable
           
            -- Select the corresponding row from deleted table
            Select @OldName = Name, @OldGender = Gender, 
            @OldSalary = Salary, @OldDeptId = DepartmentId
            from deleted where Id = @Id  --deleted table is virtual table provided by SQL Server inside triggers
   
     -- Build the audit string dynamically           
            Set @AuditString = 'Employee with Id = ' + Cast(@Id as nvarchar(4)) + ' changed'
            if(@OldName <> @NewName)  -- <> is not equal to
                  Set @AuditString = @AuditString + ', NAME from ' + @OldName + ' to ' + @NewName
                 
            if(@OldGender <> @NewGender)
                  Set @AuditString = @AuditString + ', GENDER from ' + @OldGender + ' to ' + @NewGender
                 
            if(@OldSalary <> @NewSalary)
                  Set @AuditString = @AuditString + ', SALARY from ' + Cast(@OldSalary as nvarchar(10))+ ' to ' + Cast(@NewSalary as nvarchar(10))
                  
            if(@OldDeptId <> @NewDeptId)
                  Set @AuditString = @AuditString + ', DepartmentId from ' + Cast(@OldDeptId as nvarchar(10))+ ' to ' + Cast(@NewDeptId as nvarchar(10))
           
            insert into tblEmployeeAudit values(@AuditString)  --inserting AuditString into tblEmployeeAudit Table
            
            -- Delete the row from temp table, so we can move to the next row and pick top 1
            Delete from #TempTable where Id = @Id
      End
End

update tblEmployee set Name='Geetha' where id=1


Select * from tblEmployeeAudit


update tblEmployee set Gender='Female',Salary=9000  where id=1