--Create Product table
CREATE TABLE Product
(
ProductID INT PRIMARY KEY, 
Name VARCHAR(40), 
Price INT,
Quantity INT
)


INSERT INTO Product VALUES(101, 'Product-1', 100, 10)
INSERT INTO Product VALUES(102, 'Product-2', 200, 15)
INSERT INTO Product VALUES(103, 'Product-3', 300, 20)
INSERT INTO Product VALUES(104, 'Product-4', 400, 25)


SELECT * FROM Product


--EXPLICIT TRANSACTION
BEGIN TRANSACTION
--INSERT INTO Product VALUES(105,'Product-5',500, 30)  --Inserting 105
UPDATE Product SET Price =350 WHERE ProductID = 103  --Updating 103
--DELETE FROM Product WHERE ProductID = 103  --Deleting 103
COMMIT TRANSACTION


BEGIN TRANSACTION
 BEGIN TRY
	INSERT INTO Product VALUES(106,'Product-6',600,12)  --inserts 106
	INSERT INTO Product VALUES(106,'Product-6',600,12)  --skips to catch block due to error primary key, repetition. Does not commit
	DELETE FROM Product where ProductID=102
	COMMIT TRANSACTION  --Does not commit, skips to catch block and rollback
	END TRY
BEGIN CATCH
ROLLBACK TRANSACTION  --executes
END CATCH


SELECT * FROM Product


--IMPLICIT TRANSACTION
SET IMPLICIT_TRANSACTIONS ON

CREATE TABLE Customer
(
CustomerId int primary key,
CustomerCode varchar(10),
CustomerName varchar(50)
)

SET IMPLICIT_TRANSACTIONS off


Select * from Customer
Delete from customer  --to run below batch again


SET IMPLICIT_TRANSACTIONS ON
insert into Customer values(1,'ccode-1','John')
insert into Customer values(2,'ccode-2','James')
insert into Customer values(3,'ccode-3','Peter')  --cust3 inserted

--COMMIT Transaction
--Select * from Customer

--insert into Customer values(3,'ccode-3','Peter')  --cust3 inserted
Update Customer set CustomerName='Riya' where CustomerId=1  --cust1 updated
Rollback Transaction  --no changes are commited so not displayed
Select * from Customer


----------------------------------------------------------------
Select * from Customer
SET IMPLICIT_TRANSACTIONS OFF
Delete from customer  --to run below batch again
COMMIT
GO 

SET IMPLICIT_TRANSACTIONS ON
begin transaction
insert into Customer values(1,'ccode-1','John')
insert into Customer values(4,'ccode-4','Jake')
insert into Customer values(3,'ccode-3','Peter')  --cust3 inserted
insert into Customer values(2,'ccode-2','James')
Update Customer set CustomerName='Riya' where CustomerId=1  --cust1 updated
Rollback Transaction  --no changes are commited so not displayed
Select * from Customer









