-- Project 15 - Dates, Functions 
-- Dani Rowe 

-- 1. Show the lastname, first initial, and email of all men. Order by 
--     lastname. Use the LEFT() function for the first initial.

Select lastName, 
       LEFT(firstName, 1) AS [first intial], 
       email
From Person 
WHERE gender = 'M' 
ORDER BY lastName 

-- 2. Show the lastname, email, location of '@' in the email, number of
--      characters in the email, and the host name of the email (part to 
--      the right of the @). Use the CHARINDEX(), LEN(), and RIGHT() 
--      functions.

Select LastName, 
       Email,
       CHARINDEX('@', email) AS [location of @], 
       LEN(email) AS [length of email address], 
       RIGHT(email, LEN(email)-CHARINDEX('@',email)) AS [host name]
From Person 
Order by lastname 

-- 3. Show the lastname, firstname, and year of birth for everyone. Use 
--      DATEPART (Links to an external site.)().

Select Lastname, 
       Firstname, 
       DATEPART(Year, dateOfBirth) AS [Year of Birth]
From Person 

-- 4. Show the lastname, firstname, dateOfBirth, today's date, and the 
--      estimated age in years of everyone using DATEDIFF (Links to an
--      external site.)().

Select Lastname, 
       Firstname, 
       dateOfBirth, 
       GetDate() AS [today's date], 
       DATEDIFF(Year, dateOfBirth, GETDATE()) AS [Estimated age in years]
From Person 
Order by LastName

-- 5. Show the lastname and firstname of everyone, then their dateOf 
--     Birth, the day of the week of their dateofbirth, their birthday 
--     this year, and the day of the week for their birthday this year. 
--     This will use DATEFROMPARTS (Links to an external site.)(), and 
--     DATEPART().

Select lastname, 
       firstname, 
       dateOfBirth, 
       DATEPART(WEEKDAY, dateOfBirth) AS [Day of the week of dateofBirth], 
       DATETIMEFROMPARTS(YEAR(GETDATE())), 
       MONTH(dateofbirth), 
       DAY(dateofbirth) AS [Birthday this year]
From Person 

-- 6. Show the lastname and firstname of people who were entered more
--     than 2 years ago.

Select lastname, 
       firstname 
From Person 
Where DATEDIFF(YEAR, entryDate, GETDATE()) > 2

-- 7. Show the lastname, firstname, and email of all people whose email
--      is NULL. Also show in the same table people whose salutory is 
--      blank, i.e., an empty string. Be aware that NULL is not the same 
--      as blank - each must be checked separately.

Select lastname, 
       firstname, 
       email
From Person 
Where email = '' or email is null

-- 8. We need to check our data for inconsistencies. In one SELECT 
--      statement, find the ID of every person whose record was updated 
--      prior to their creation date, or whose weight is less than zero.

Select ID 
From Person 
Where LastupdateDate < Dateadd(year, -1, GETDATE()) or weight < 0 

-- 9. Give a count of people, by Year of birth. Also provide the average 
--      weight of people for each year.

Select YEAR(dateofbirth) AS [Year of Birth], 
       COUNT(ID) AS [Count of People], 
       AVG(weight) As [average weight of people]
From Person 
Group By YEAR(dateofbirth)
Order by YEAR(dateofbirth)

-- 10. Give a count of people, by Month of birth. Also provide the average
--      weight of people for each month.

Select DATEPART(Month, dateofbirth) AS [Month of Birth], 
       COUNT(ID) AS [Count of People], 
       AVG(weight) AS [Average Weight]
From Person 
Group by DATEPART(month, dateofbirth)
Order by DATEPART(month, dateofbirth)

