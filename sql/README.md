## 基础知识

### exchange every two values
```
SELECT ( CASE
           WHEN MOD(tb1.id, 2) != 0
                AND tb1.id != tb2.cnt THEN tb1.id + 1
           WHEN MOD(id, 2) != 0
                AND tb1.id = tb2.cnt THEN id
           ELSE id - 1
         end ) AS id,
       student
FROM   seat AS tb1,
       (SELECT Count(*) AS cnt
        FROM seat) AS tb2
ORDER  BY id ASC;
```


