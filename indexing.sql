----INDEXING----
--CLUSTERED & NON-CLUSTERED--

CREATE TABLE tbl_Employee
(
Id INT,
Name VARCHAR(50),
Salary INT,
Gender VARCHAR(10),
City VARCHAR(50),
Dept VARCHAR(50)
)

INSERT INTO tbl_Employee VALUES (3,'Pranaya', 4500, 'Male', 'New York', 'IT')
INSERT INTO tbl_Employee VALUES (1,'Anurag', 2500, 'Male', 'London', 'IT')
INSERT INTO tbl_Employee VALUES (4,'Priyanka', 5500, 'Female', 'Tokiyo', 'HR')
INSERT INTO tbl_Employee VALUES (5,'Sambit', 3000, 'Male', 'Toronto', 'IT')
INSERT INTO tbl_Employee VALUES (7,'Preety', 6500, 'Female', 'Mumbai', 'HR')
INSERT INTO tbl_Employee VALUES (6,'Tarun', 4000, 'Male', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (2,'Hina', 500, 'Female', 'Sydney', 'HR')
INSERT INTO tbl_Employee VALUES (8,'John', 6500, 'Male', 'Mumbai', 'HR')
INSERT INTO tbl_Employee VALUES (10,'Pam', 4000, 'Female', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (9,'Sara', 500, 'Female', 'London', 'IT')

SELECT * FROM tbl_Employee where Id=7

CREATE CLUSTERED INDEX idx_Employee_Id ON Tbl_Employee(id)

DROP INDEX idx_Employee_Id ON tbl_Employee

INSERT INTO tbl_Employee VALUES (19,'Pam', 4000, 'Female', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (11,'Sara', 500, 'Female', 'London', 'IT')
INSERT INTO tbl_Employee VALUES (15,'Pam', 4000, 'Female', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (13,'Sara', 500, 'Female', 'London', 'IT')

CREATE Unique INDEX idx_uniqueid ON tbl_Employee(id)

-----------------------------------------------------------------

/* To declare variable and 
Loop it */

CREATE Table tblOrder
(Id INT,
CustomerId INT,
ProductID varchar(50),
ProductName varchar(50)
)

DECLARE @i int=1
WHILE @i<4000
BEGIN
SET @i=@i+1
	IF(@i<1000)
	BEGIN
	INSERT INTO tblOrder values (@i,1,'Product-101','iPad Air')
	END
	ELSE IF(@i<2000)
	BEGIN
	INSERT INTO tblOrder values (@i,3,'Product-3001','Lenova Think Pad')
	END
	ELSE IF(@i<3000)
	BEGIN
	INSERT INTO tblOrder values (@i,2,'Product-100','Wireless Keyboard')
	END
	ELSE IF(@i<4000)
	BEGIN
	INSERT INTO tblOrder values (@i,1,'Product-300','Tablet')
	END
END

select count(*) from tblOrder

SELECT * FROM tblOrder WHERE ProductID='Product-3001' AND CustomerId=3

CREATE NONCLUSTERED INDEX idx_tblOrder_pid
ON tblOrder(ProductId)
INCLUDE([Id],[CustomerId],[ProductName])

SELECT * FROM tblOrder WHERE ProductID='Product-100'
























