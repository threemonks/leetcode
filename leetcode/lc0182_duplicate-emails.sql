/*
182. Duplicate Emails
Easy

714

39

Add to List

Share
SQL Schema
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
*/
Create table Person (
    Id INT,
    Email VARCHAR(100)
);
Insert into Person (Id, Email) Values
(1, 'a@b.com'),
(2, 'c@d.com'),
(3, 'a@b.com')

# Write your MySQL query statement below
select Email
from (
select Email, count(*) as email_count
    from Person
group by Email
) a where email_count > 1;

-- or

Select Email from Person
group by Email
having count(*) > 1;