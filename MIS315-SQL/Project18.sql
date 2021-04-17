-- Project 18 - Dates, Functions 
-- Dani Rowe 

-- 1. Insert yourself into the Person table. Use your firstName, lastName,
--     and your UNCW userName. Leave the ID blank - it will be filled in
--     with a unique number by the database.

INSERT INTO Person
              (firstname, 
              lastname,
              userName)
VALUES ('Danielle', 
       'Rowe')

-- 2. Insert yourself into the Student table. Find your Person.ID 
--     (using a SELECT statement?). Insert your personID and the year you
--      entered UNCW.

INSERT INTO Student 
              (yearOfUniversityEntry,
              studentID)
VALUES (2019, 850499723)
INSERT INTO Person
              (personID)
VALUES (110)

--3. Insert yourself into the ClassMember table as a member of the Fall
--      2019 MIS315 class. Use your Student.personID, and figure out the 
--      correct ClassSection by running this query:
--           SELECT *
--           FROM   ClassesAndStudents

INSERT INTO ClassMember 
              (ClassMemberID, 
              StudentID, 
              ClassSectionID, 
              DateofRegistration)
VALUES (850, 850499723, 001, 2019)

-- 4. Choose another class that you are enrolled in this semester. Make
--       sure this class does not yet exist in the ClassSection table. 
--       Insert a record for that class (with the appropriate instructor),
--       and insert yourself into the ClassMember table as a member of 
--       the class. Make sure that all necessary records are in the 
--       necessary tables. This is likely to require multiple statements. 
--       For example, suppose you are enrolled in ACG203.002 right now.
--       You may have to INSERT a record in Department for the Accounting
--       and Business Law department, then a record in Subject for ACG,
--       then a record in Course for ACG203, then a record in Person and
--       Instructor for the instructor, then a record into ClassSection 
--       for ACG203.002, then insert yourself. At a minimum, you should
--       have an INSERT into the ClassSection table, and an INSERT into 
--       the ClassMember table.

INSERT INTO ClassSection
              (courseID, 
              termID,
              sectionNumber,
              instructorID)
VALUES ('72',
       '88',
       '002',
       '27')

INSERT INTO ClassMember
              (studentID, 
              classsSectionid)
VALUES ('976',
       '828')
