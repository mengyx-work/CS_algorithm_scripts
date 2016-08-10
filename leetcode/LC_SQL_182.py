## detailed introduction on this topic
## http://www.w3resource.com/mysql/advance-query-in-mysql/find-duplicate-data-mysql.php
SELECT Email
FROM Person
GROUP BY Email
HAVING Count(Id) > 1
