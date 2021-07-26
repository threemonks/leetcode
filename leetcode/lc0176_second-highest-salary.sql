/*
176. Second Highest Salary
Easy

1250

595

Add to List

Share
SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/

Create table Employee(
    Id INT,
    Salary INT
);
Insert into Employee (Id, Salary) Values
(1, 100),
(2, 200),
(3, 300),
(4, 200);

# Write your MySQL query statement below

Select Max(Salary) AS SecondHighestSalary
From Employee
Where Salary < (Select Max(Salary) From Employee);

-- or

SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;