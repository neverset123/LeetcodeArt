## 使用union比where A or B要高效
## update table 
```
update Salary
set sex=if(sex="m", "f", "m")
```
## check odd and even
```
id%2
或者
mod(id, 2)
```
## get null row
```
where id is null
```
## DATEDIFF(expr1,expr2)可以求解行间差
## delete duplicates
```
delete p1 
from Person p1, Person p2
where p1.email=p2.email and p1.Id > p2.Id
```

## select second largest
```
limit 1 offset 1
```
## swap value
```
SELECT ( CASE
           WHEN MOD(id, 2) != 0
                AND counts != id THEN id + 1
           WHEN MOD(id, 2) != 0
                AND counts = id THEN id
           ELSE id - 1
         end ) AS id,
       student
FROM   seat,
       (SELECT Count(*) AS counts
        FROM   seat) AS seat_counts
ORDER  BY id ASC;;
```

## dense rank
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as `rank`
FROM Scores

