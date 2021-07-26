/*
1112. Highest Grade For Each Student
Medium

130

4

Add to List

Share
SQL Schema
Table: Enrollments

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) is the primary key of this table.

Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id. The output must be sorted by increasing student_id.

The query result format is in the following example:

Enrollments table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+

Result table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+

*/
# Write your MySQL query statement below
select student_id, min(course_id) as course_id, grade
from
(
    select e.student_id, e.course_id, e.grade
    from Enrollments e
    join
    (
        select student_id, max(grade) as max_grade
        from Enrollments
        group by student_id
    ) mg on e.student_id = mg.student_id and e.grade = mg.max_grade
) a
group by student_id, grade
order by student_id asc
