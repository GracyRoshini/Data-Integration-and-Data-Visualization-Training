Use bikestores;
GO

----ASSIGNMENT-1

/* Question 1:
The Marketing Team needs a view of active products where model_year > 2018.
The view should include product_id, product_name, brand_name, category_name, and list_price.
Use appropriate joins to get brand and category details.
Sort the result by category_name and then by product_name */

CREATE VIEW vwProductCatalog AS
SELECT 
    p.product_id,
    p.product_name,
    b.brand_name,
    c.category_name,
    p.list_price
FROM 
    production.products p
JOIN 
    production.brands b ON p.brand_id = b.brand_id
JOIN 
    production.categories c ON p.category_id = c.category_id
WHERE 
    p.model_year > 2018;

SELECT * 
FROM vwProductCatalog
ORDER BY category_name, product_name;

------------------------------------------------------------------------------------------

/* Question 2:
The Inventory Team wants to track unsold products.
Create a view that lists all products that have never been sold
Then, write a query that ranks these unsold products within each category by list price in descending order,and returns only the top-ranked product per category.
Expected Output: category_name, product_name, list_price — one row per category */
CREATE VIEW vwUnsoldProducts AS
SELECT 
    p.product_id,
    p.product_name,
    c.category_name,
    p.list_price
FROM 
    production.products p
JOIN 
    production.categories c ON p.category_id = c.category_id
WHERE 
    NOT EXISTS (
        SELECT 1 
        FROM sales.order_items oi 
        WHERE oi.product_id = p.product_id
    );


WITH RankedProducts AS (
    SELECT 
        category_name,
        product_name,
        list_price,
        RANK() OVER (PARTITION BY category_name ORDER BY list_price DESC) AS rnk
    FROM 
        vwUnsoldProducts
)--SELECT * from RankedProducts
    Select category_name,
    product_name,
    list_price, rnk
FROM 
    RankedProducts
WHERE 
    rnk = 1;