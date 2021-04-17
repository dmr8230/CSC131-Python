-- Project 13 RANK
-- Dani Rowe 

-- 1. Show each productname, then the ROW_NUMBER, RANK, DENSE_RANK and NTILE(4) based 
--     on unitprice.

Select ProductName, 
       ROW_Number() OVER (ORDER BY UnitPrice) AS [ROW], 
       RANK() OVER (ORDER BY UnitPrice) AS [RANK], 
       DENSE_RANK() OVER (ORDER BY UnitPrice) AS [DRank],
       NTILE(4) OVER (ORDER BY UnitPrice) AS [Pctile]
From Products 
ORDER BY ProductName 

-- 2. Show a list of products, their unit price, and their ROW_NUMBER() based on
--     unitprice, ASC. Order the records based on productname.

Select ProductName, 
       UnitPrice, 
       ROW_NUMBER() OVER (ORDER BY UnitPrice ASC) AS [ROW]
From Products 
ORDER BY ProductName 

-- 3. Show a list of products, their unit price, and their DENSE_RANK() based on
--     unitprice, ASC. Order the records based on productname.

Select ProductName, 
       UnitPrice, 
       DENSE_RANK() OVER (ORDER BY UnitPrice ASC) AS [DRank]
From Products 
ORDER BY ProductName 

--4. Show a list of products, their unitsinstock, and their RANK() based on
--     unitsinstock, ASC. Order the records based on productname.

Select ProductName, 
       UnitsInStock, 
       RANK() OVER (ORDER BY UnitsInStock ASC) AS [RANK]
FROM Products 
ORDER BY ProductName 

--5. Show a list of products, their inventory value (unitsInStock*unitprice), and
--     their RANK() based on inventory value, highest to lowest. Order the records by
--     inventory value.

Select ProductName, 
       UnitsInStock*UnitPrice AS [Inventory Value], 
       RANK() OVER (ORDER BY UnitsInStock*UnitPrice DESC) AS [RANK]
From Products 
ORDER BY UnitsInStock*UnitPrice 

--6. Show a list of products, categoryID, and their unitprice. Also show their dense
--     rank within their category based on unitprice highest to lowest. Order by 
--     CategoryID, then unitprice desc.

Select ProductName,
       CategoryID, 
       UnitPrice,
       DENSE_RANK() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC) AS [DRank by Category] 
From Products 
ORDER BY CategoryID, 
        UnitPrice DESC 

-- 7. Show a list of products, supplierID, and unitprice. Also show their ROW_NUMBER 
--     compared to other products from the same supplier, based on unitprice highest 
--     to lowest. order by SupplierID, then unitprice desc.

Select ProductName, 
       SupplierID, 
       UnitPrice, 
       ROW_NUMBER() OVER (PARTITION BY SupplierID ORDER BY UnitPrice DESC) AS [Row by Product] 
From Products 
Group by ProductID -- correct way to compare to other suppliers? 
Order by SupplierID,
         UnitPrice DESC 

-- 8. Rank (NTILE()) all products by inventory value: 1 = high $ in inventory,
--     2=medium $ in inventory, 3=low $ in inventory. Order by RANK(), then by 
--     productname.

Select NTILE(3) OVER (ORDER BY UnitsInStock*UnitPrice DESC) AS [Pctile]
From Products 
Order by ProductName

-- 9. Show each OrderID, the freight, and the RANK() for each order based on freight.

Select OrderID, 
       Freight, 
       RANK() OVER (ORDER BY Freight) AS [RANK]
From Orders 
ORDER BY OrderID 

-- 10. Show each OrderID, the shipper, the freight, and the RANK() for each order
--     based on freight compared to the same shipper.

Select OrderID, 
       ShipperName, 
       Freight, 
       RANK() OVER (PARTITION BY ShipName ORDER BY Freight) AS [RANK]
From Orders 
Order by OrderID 
