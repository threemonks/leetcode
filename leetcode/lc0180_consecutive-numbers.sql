/*
180. Consecutive Numbers
Medium

661

149

Add to List

Share
SQL Schema
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.


Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example:



Logs table:
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Result table:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
1 is the only number that appears consecutively for at least three times.

*/

Create table Logs(
    Id INT,
    Num INT
);
Insert into Logs (Id, Num) Values
(1,1),
(2,1),
(3,1),
(4,2),
(5,1),
(6,2),
(7,2);

# Write your MySQL query statement below
SELECT DISTINCT num ConsecutiveNums
FROM
(
    SELECT id, num,
    LAG(num) OVER (ORDER BY id) AS prev_num,
    LEAD(num) OVER (ORDER BY id) as next_num
    FROM logs
) next_prev
WHERE num=prev_num AND prev_num = next_num