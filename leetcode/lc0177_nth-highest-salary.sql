/*
177. Nth Highest Salary
Medium

695

513

Add to List

Share
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

rank() vs dense_rank()
if there are ties, dense_rank() always returns consecutive integers, while rank() returns discrete ones.

ROW_NUMBER() vs RANK() vs DENSE_RANK()
ROW_NUMBER() attributes a unique value to each row
RANK() attributes the same row number to the same value, leaving "holes"
DENSE_RANK() attributes the same row number to the same value, leaving no "holes"

*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee
      order by Salary desc
      limit 1 OFFSET M
  );
END

Select Id, Salary, Rank() Over (Order by Salary Desc) From Employee;
Select Id, Salary, Dense_Rank() Over (Order by Salary Desc) From Employee;

Select Distinct Salary From (
    Select Id, Salary, Rank() Over (Order by Salary Desc) From Employee
    ) tmp
Where Rank=N;