### ROW_NUMBER() vs RANK() vs DENSE_RANK()
- OW_NUMBER() attributes a unique value to each row
- RANK() attributes the same row number to the same value, leaving "holes"
- DENSE_RANK() attributes the same row number to the same value, leaving no "holes"

### Escape reversed keyword
SELECT Score as score, DENSE_RANK() OVER (ORDER BY Score DESC) AS `Rank` FROM Scores

### Window Function
The LEAD() and LAG() function in MySQL are used to get preceding and succeeding value of any row within its partition.
The LAG() function is used to get value from row that precedes the current row.
The LEAD() function is used to get value from row that succedes the current row.
Syntax: LEAD(expr, N, default)
          OVER (Window_specification | Window_name)
        LAG(expr, N, default)
          OVER (Window_specification | Window_name)
e.g. Select c_id, start_date, end_date,
        end_date - lead (start_date)
        over (order by start_date)
               + 1 as 'no_of_days'
                   from contest;

### Recursive self join - employees whose direct or indirect manager (up to 3 levels) are employee id 1
SELECT e1.employee_id
FROM Employees e1,
     Employees e2,
     Employees e3
WHERE e1.manager_id = e2.employee_id
  AND e2.manager_id = e3.employee_id
  AND e3.manager_id = 1
  AND e1.employee_id != 1

### Generate number sequence
WITH T AS (
SELECT ROW_NUMBER() OVER() row_num
FROM Transactions
UNION
SELECT 0
)

### Date function- DATEDIFF(expr1, expr2)
- DATEDIFF() returns expr1 − expr2 expressed as a value in days from one date to the other.

### Pivot table
SELECT id,
SUM(IF(month='Jan', revenue, NULL)) AS Jan_Revenue,
SUM(IF(month='Feb', revenue, NULL)) AS Feb_Revenue,
SUM(IF(month='Mar', revenue, NULL)) AS Mar_Revenue,
SUM(IF(month='Apr', revenue, NULL)) AS Apr_Revenue,
SUM(IF(month='May', revenue, NULL)) AS May_Revenue,
SUM(IF(month='Jun', revenue, NULL)) AS Jun_Revenue,
SUM(IF(month='Jul', revenue, NULL)) AS Jul_Revenue,
SUM(IF(month='Aug', revenue, NULL)) AS Aug_Revenue,
SUM(IF(month='Sep', revenue, NULL)) AS Sep_Revenue,
SUM(IF(month='Oct', revenue, NULL)) AS Oct_Revenue,
SUM(IF(month='Nov', revenue, NULL)) AS Nov_Revenue,
SUM(IF(month='Dec', revenue, NULL)) AS Dec_Revenue
FROM Department
GROUP BY id;