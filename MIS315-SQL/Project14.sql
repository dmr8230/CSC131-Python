--Project 14 – Character Manipulation, Functions 
-- Dani Rowe 

-- 1. Select the ProductID, ProductName, and one more column. The last 
--     column should be titled "InStock/OnOrder". The contents should be 
--     a varchar that has the unitsinstock, then a forward slash, then 
--     the unitsOnOrder. So it should look like this: 32/10

Select productID, 
       productName, 
       CONVERT(VARCHAR, UnitsInStock)
              + '/'
              + CONVERT(VARCHAR,UnitsOnOrder) AS [InStock/OnOrder]
From Products 
ORDER BY productID 

--2. Select the productID, productname, and one more column. Only show 
--     products whose unitsInStock are below their reorderlevel. 
--     The last column should be titled "Amount to Order". The number 
--     in the columns should be the number of units to bring the 
--     UnitsInstock up to 2 times the reorderlevel. So if the 
--     UnitsInStock is 8, and the reorderLevel is 20, then the Amount to 
--     order would be 32. In other words: (20 * 2) - 8.

 Select ProductID, 
        ProductName,
        UnitsInStock, 
        ReorderLevel,
        2 * ReorderLevel - UnitsInstock AS [Amount to Order ]
From Products 
Order by ProductID 

--3.Select the ProductID, ProductName, and the location of the first 
--     space in the productName. Use the CHARINDEX (Links to an external 
--     site.) function.

Select ProductID, 
       ProductName,
       CHARINDEX(' ', ProductName) AS [first space location]
From Products 
Order by ProductID

--4.Show the ProductName, then a column that has the productID and 
--     CategoryID concatenated together like this: 18(2).

Select ProductID, 
       ProductName, 
       CONCAT(ProductID, '(', CategoryID, ')') AS [prodID(catID)]
From Products 
Order by ProductID 

--5.Our new system cannot handle the hyphens in the QuantityPerUnit field,
--     so we need to replace all hyphens in this field with the lower
--     case x. Show the ProductID in the first column, the current 
--     QuantityPerUnit, and the new QuantityPerUnit with all hyphens 
--     replaced with an x. Use the REPLACE (Links to an external site.) 
--     function.

Select ProductID,
       QuantityPerUnit, 
       REPLACE(QuantityPerUnit, '-', 'x') AS [newQtyPerUnit]
From Products
Order by ProductID 

--6.Our new system cannot handle Unicode (Links to an external site.) 
--     characters, only ASCII (Links to an external site.) characters. 
--     The current Productname data type is NVARCHAR, which is unicode, 
--     and might have non-ASCII characters in it. We need to check! Show 
--     the ProductID, and ProductName, and the first location of any
--     non-Unicode characters. See the note at the bottom for how to find
--     non-Unicode characters. 

Select ProductID,
       QuantityPerUnit, 
       CHARINDEX('?', CONVERT(VARCHAR, ProductName)) AS [1st Unicode location]
From Products 
Order by ProductID 

--7.We'd like to make up a new productCode for human use. It's going to be
--     made up of the CategoryID, the SupplierID, and the ProductID with
--     hyphens between them, something like this: 2-12-77. Use the 
--     CONCAT_WS (Links to an external site.) function to do this. Show 
--     the CategoryID, the SupplierID, the ProductID, and the new 
--     ProductCode column.

Select CategoryID, 
       SupplierID, 
       ProductID, 
       CONCAT_WS('-', CategoryID, SupplierID, ProductID) AS [ProductCode]
From Products 
Order by ProductID 

--8. Our invoices can only show 20 characters for the Product. We'd like 
--     this to be made up of the left-most 15 characters of the 
--     ProductName, then a forward slash, then the leftmost 4 characters
--     of the QuantityPerUnit. Use the LEFT (Links to an external site.) 
--     function to help out. Show the ProductID, ProductName, 
--     QuantityPerUnit, and the new column, named ProductDescription.

Select ProductId, 
       ProductName, 
       QuantityPerUnit, 
       --CONVERT(VARCHAR(15), ProductName)
              -- + '/', 
              -- + CONVERT(VARCHAR(4), QuantityPerUnit 
              -- AS [ProductDescription]
       LEFT(productname, 4)
              + '/' 
              + LEFT(QuantityPerUnit, 4)
From Products 
Order by ProductID 

--9. Oops, we messed up the logic on question #2 above. We might already
--      have some units on order! Re-do #2. Only show products where the
--     (UnitsInStock+UnitsOnOrder) is less than the ReorderLevel. For 
--     these products, calculate the Amount to order as (2*ReorderLevel)
--      - (UnitsInStock+UnitsOnOrder).

Select ProductID, 
       ProductName,
       2 * ReorderLevel - (UnitsInStock + UnitsOnOrder) AS [Amount to Order]
FROM Products 
Where 2 * ReorderLevel - (UnitsInStock+UnitsOnOrder) > 0 
Order by ProductID 

--10. Our new system cannot handle Unicode characters in the ProductName
--      or QuantityPerUnit columns. Use the CONVERT function to show the 
--      ProductID, then the current ProductName, then the ProductName 
--      converted from to VARCHAR. Do the same for QuantityPerUnit.

Select ProductID,
       ProductName, 
       CONVERT(VARCHAR, ProductName) AS [ASCII ProductName], 
       QuantityPerUnit,
       CONVERT(VARCHAR, QuantityPerUnit) AS [ASCII QuantityPerUnit]
From Products 
-- WHERE CHARINDEX('?', CONVERT(VARCHAR,ProductName)) > 0 
--    OR CHARINDEX('?', CONVERT(VARCHAR,QuantityPerUnit)) > 0 
Order by ProductID 
