-- Project 16 - Subqueries 
-- Dani Rowe 

-- 1. Give all details (use *) about the product with the lowest unit 
--       price. (Use unitprice from the products table).

Select * 
From Products 
Where UnitPrice = 
   (SELECT MIN(unitprice)
   FROM Products)
ORder by ProductID ASC

-- 2. Give all details about all below average price products( Use 
--       unitprice from the products table).

Select * 
From Products 
Where UnitPrice < 
   (Select AVG(UnitPrice) 
   FROM Products) 
Order by ProductID ASC

-- 3. Give all details about the order with the highest freight.

Select * 
From Orders
Where Freight = 
   (Select MAX(Freight)
   From Orders) 
Order by OrderID ASC

-- 4. Give all details about orders with above average freight costs.

Select * 
From Orders 
Where Freight > 
   (Select AVG(Freight)
   FROM Orders)
Order by OrderID ASC

-- 5. Give all details about the product(s) with the minimum reorderlevel.

Select * 
From Products
Where Reorderlevel = 
   (Select MIN(reorderlevel)
   FROM products)
Order by ProductID ASC 

-- 6. Give all details about products with below average reorderlevels.

Select * 
From Products 
Where Reorderlevel <
   (Select AVG(reorderlevel)
   FROM products)
Order by ProductID ASC 

-- 7. Give all details about the product with the most units in stock.

Select * 
From Products 
Where UnitsInStock = 
   (Select MAX(UnitsInStock)
   FROM products)
Order by ProductID ASC 

-- 8. Give all details about the products with above average units in 
--      stock.

Select * 
From Products 
WHERE UnitsInStock > 
   (Select AVG(UnitsInStock)
   FROM products)
Order by ProductID ASC 

-- 9. Give all details about the product with the highest total dollar 
--      value in inventory.

Select * 
From Products 
Where  UnitsInStock * UnitPrice = 
   (Select MAX(UnitsInStock * UnitPrice)
   FROM products) 
Order by ProductID ASC 

-- 10. Give all details about products with above average dollar value in 
--      inventory.

Select * 
From Products 
Where UnitsInStock * UnitPrice > 
   (Select AVG(UnitsInStock * UnitPrice)
   From Products)
ORder by ProductID ASC 
