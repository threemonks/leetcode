/*
183. Customers Who Never Order
Easy

582

58

Add to List

Share
SQL Schema
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/

Create table Customers (
    Id INT,
    Name VARCHAR(50)
);
Create table Orders (
    Id INT,
    CustomerId INT
);
Insert into Customers (Id, Name) Values (1, 'Joe'), (2, 'Henry'), (3, 'Sam'), (4, 'Max');
Insert into Orders (Id, CustomerId) Values (1, 3), (2, 1);

# Write your MySQL query statement below
select c.Name as Customers
from Customers c
left join Orders o
on c.Id = o.CustomerId
where o.Id is null