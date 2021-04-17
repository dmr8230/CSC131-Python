-- Project 17 - Subqueries 
-- Dani Rowe 

-- 1. Insert a new person whose name is Jonathon Smith. His nickname is 
--      Jack. Leave all the other fields empty. Use the safe form of the
--      INSERT statement, where you specify every field that you will 
--      provide a value for.

INSERT INTO tblPerson 
            (Firstname, 
            Lastname, 
            nickname)
Values ('Jonathon', 
         'Smith', 
         'Jack')

-- 2. Update Jack's cell phone number to 987-456-1234. Don't change any 
--      other field. Make sure you only change Jack's cell phone by having
--      the right PersonID=? in the WHERE clause.

UPDATE tblPerson
SET Phonecell = '987-456-1234'
Where PersonID = 10000

-- 3. Insert a new person whose name is Deborah Jones. Her nickname is
--       Debbie. Leave all the other fields empty. Use the safe form of
--       the INSERT statement, where you specify every field that you will
--       provide a value for.

INSERT INTO tblperson 
            (firstname, 
            lastname, 
            nickname)
VALUES ('Deborah', 
         'Jones', 
         'Debbie')

-- 4. Update Debbie's nickname to Deb. Don't change any other field. Make
--      sure you only change Debbie's nickname by having the right 
--      PersonID=? in the WHERE clause.

UPDATE tblperson 
SET nickname = 'Deb'
WHERE personID = 10001

-- 5. Give Jack the Student/Alumni role. You do this by inserting a record
--      into the tblPersonRoles table. Use Jack's perID. Use roleID of 1 
--      (refer to validPersonRoles to see that this the Student/Alumni 
--       role.)

INSERT INTO tblPersonRoles
            (roleID, 
            PerID)
VALUES (1, 10000)

-- 6. Give Jack the Grad Asst role (yes, Jack can have two roles). Look up
--      the right roleID for Grad Asst in the validPersonRoles table.

INSERT INTO tblPersonRoles
            (RoleID, 
            PerID)
VALUES (89, 10000) 

-- 7. Delete Deb from the database. Make sure you only delete Deb's record
--      by having the right PersonID=? in the WHERE clause.

DELETE 
FROM tblPerson 
WHERE PersonID = 10001

-- 8. We need to put Jack's mother into the system. This will take two 
--     separate operations: and insert into tblPerson, and an insert into 
--     tblPersonRoles. Write both statements. Jack's mom's name is Karen
--     Smith and her nickname is Kay.

INSERT INTO tblPerson
            (firstname, 
            lastname, 
            nickname)
VALUES ('Karen', 
         'Smith', 
         'Kay')
INSERT INTO tblPersonRoles
            (RoleID, 
            PerID)
VALUES (21,10002)

-- 9. Enter a new person named David Johnson with the nickname of Dave and
--     phone number 765-867-5309 who is a CEN mentor and a Business Week
--     presenter. Make sure to give the proper roles to David.

INSERT INTO tblPerson 
            (firstname, 
            lastname, 
            nickname, 
            Phonecell)
VALUES ('David', 
         'Johnson', 
         'Dave',
         '765-867-5309')
INSERT INTO tblPersonRoles
            (PerID, 
            roleID)
VALUES (10003, 46)

-- 10. Enter a new person named Diane Kincaid with the nickname DeeDee. 
--     She is an ISOM advisory board member, a CEN mentor, a Business Week
--     presenter, and a Guest Lecturer.

INSERT INTO tblPerson
            (firstname,
            lastname, 
            nickname)
VALUES ('Diane', 
         'Kincaid',
         'DeeDee')
INSERT INTO tblPersonRoles 
            (perID, 
            roleID)
Values (10004,31)
INSERT INTO tblPersonRoles 
            (perID, 
            roleID)
Values (10004,26)
INSERT INTO tblPersonRoles 
            (perID, 
            roleID)
Values (10004,46)

