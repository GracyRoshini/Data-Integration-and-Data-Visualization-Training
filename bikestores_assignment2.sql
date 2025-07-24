--Task1
/* Write a scalar-valued function that takes a product_id as input 
and returns the list_price of that product */
 
alter Function FN_GetListPrice(@product_id int)
returns decimal(10,2)
as
Begin
Declare @ListPrice decimal(10,2);  --Local variable to store list_price
select @ListPrice=list_price
from production.products
where product_id=@product_id;  --for user input
return @ListPrice
END

SELECT dbo.FN_GetListPrice(70)

------------------------------------------------
--Task2
/* Write an inline table-valued function that returns all products 
for a given category_id */

Create Function GetProductsByCategory(@category_id int)
RETURNS Table
AS
Return (Select product_id, product_name, list_price,brand_id,category_id
        from production.products
        where category_id=@category_id)

Select * from dbo.GetProductsByCategory(4);
--------------------------------------------------
--Task3
/* Create a function that takes a store_id & returns the total sales 
amount for that store. Use the 'sales.orders' & 'sales.order_items' tables. 
Sum the list_price * quantity for all orders from that store*/

Create Function GetTotalSalesByStore(@store_id INT)
Returns Decimal(10,2)
AS
Begin
Declare @totalamt decimal(10,2)
Select @totalamt= SUM(oi.list_price * oi.quantity)
from sales.orders o
INNER JOIN sales.order_items oi 
ON o.order_id=oi.order_id
Where o.store_id=@store_id
Return ISNULL(@totalamt,0)
END

SELECT dbo.GetTotalSalesByStore(3) AS TotalSales;

------------------------------------------------
--Task4
/* Write a table-valued function that takes two dates as input and 
returns all orders placed between those dates */

Create Function GetOrdersBtwDates(@start_date Date, @end_date Date)
Returns table
AS
Return (
        Select order_id, customer_id, order_date, store_id
        from sales.orders
        where order_date BETWEEN @start_date AND @end_date)

Select * from GetOrdersBtwDates('2016-10-01' , '2016-10-10');

------------------------------------------------
--Task5
/* Write a function that takes a brand_id and 
returns the number of products for that brand */

Create Function GetProductCountByBrand(@brand_id INT)
RETURNS int
AS
BEGIN
Declare @count INT
Select @count=COUNT(*)
From production.products
Where brand_id=@brand_id
Return @count
End

Select dbo.GetProductCountByBrand(2) as ProductCount  --Scalar (dbo)

---------------------------------------------------