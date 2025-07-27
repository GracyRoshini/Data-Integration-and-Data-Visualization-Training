/* Create a trigger that logs any update to the list_price 
of a product in the production.products table */

Create Table production.price_change_log( log_id int Identity(1,1) Primary key,
                                          product_id int not null, 
                                          old_price Decimal(10,2) not null,
                                          new_price Decimal(10,2) not null,
                                          change_date datetime Not null Default GETDATE());


SELECT * FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'products';


alter TRIGGER production.trg_log_price_change
ON production.products  -- ← Use your actual schema
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;  --to eliminate 'N' rows returned msg

    INSERT INTO production.price_change_log (product_id, old_price, new_price)
    SELECT
        i.product_id,
        d.list_price AS old_price,
        i.list_price AS new_price
    FROM
        inserted i
    INNER JOIN
        deleted d ON i.product_id = d.product_id
    WHERE
        i.list_price <> d.list_price;
END;


--2. Trigger to Prevent Deletion of Products Used in Open Orders
Create Trigger trg_prevent_product_delete
On production.products
Instead Of Delete
As
Begin
    Set NOCOUNT ON;  --to eliminate 'N' rows affected msg

    If exists (
        Select 1
        From deleted d
        Inner join sales.order_items oi
        ON d.product_id =oi.product_id
        Inner Join sales.orders o
        ON oi.order_id =o.order_id
        Where o.order_status IN (1,2))  --Order status: 1 = Pending; 2 = Processing
    Begin
        RAISERROR('Cannot delete products involved in open orders',16,1); --16 is severity level, 1 is state code
        RollBack Transaction;
        Return;
    END

    Delete from production.products
    Where product_id IN (Select product_id From deleted)
END


/* cmd to check if trigger exist
SELECT name, parent_class_desc, OBJECT_NAME(parent_id) AS table_name
FROM sys.triggers
WHERE name = 'trg_log_price_change'; */


/* cmd to drop trigger
DROP TRIGGER production.trg_log_price_change; */ -- use schema if needed

---------------------------------------------------------------------------------------------------------------------------------

/* 1) Total Sales by Store (Only High-Performing Stores)
List each store's name and the total sales amount (sum of quantity × list price) 
for all orders. Only include stores where the total sales amount exceeds $50,000 */

Select s.store_name, Sum(oi.quantity * oi.list_price) AS total_sales
From sales.stores s
INNER JOIN sales.orders o
ON s.store_id = o.store_id
INNER JOIN sales.order_items oi 
ON o.order_id=oi.order_id
Group By s.store_name
Having Sum(oi.quantity * oi.list_price) > 50000;

/* 2) Top Selling Products by Quantity 
Find the top 5 best-selling products by total quantity ordered */

Select Top 5 p.product_name, Sum(oi.quantity) As total_quantity_sold
From production.products p
INNER JOIN sales.order_items oi 
ON p.product_id =oi.product_id
Group By p.product_name
Order By total_quantity_sold Desc;

/* 3) how monthly sales totals (sum of line total) for the year 2016 */

Select Format(o.order_date, 'yyyy-MM') As month,
       Sum(oi.quantity * oi.list_price) As monthly_sales
From sales.orders o
INNER JOIN sales.order_items oi
ON o.order_id=oi.order_id
Where Year(o.order_date) =2016
Group By Format(o.order_date, 'yyyy-MM')
Order By month;

/* 4) High Revenue Stores
List all stores whose total revenue is greater than ₹1,00,000 */

Select s.store_name, Sum(oi.quantity * oi.list_price) As total_revenue
From sales.stores s
INNER JOIN sales.orders o 
ON s.store_id=o.store_id
INNER JOIN sales.order_items oi
ON o.order_id = oi.order_id
Group By s.store_name
Having Sum(oi.quantity * oi.list_price) > 100000;




























