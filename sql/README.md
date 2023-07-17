## 基础知识
### 使用union比where A or B要高效
### update table 
```
update Salary
set sex=if(sex="m", "f", "m")
```
### check odd and even
```
id%2
或者
mod(id, 2)
```
### get null row
```
where id is null
```
### delete duplicates
```
delete p1 
from Person p1, Person p2
where p1.email=p2.email and p1.Id > p2.Id
```

### select second largest
```
limit 1 offset 1
```
### exchange every two values
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

### dense rank
返回的是持续的编号
```
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as `rank`
FROM Scores
```
### 处理空值
ISNULL(expr)  如果expr为null返回值1，否则返回值为0
IFNULL(expr1,expr2) 如果expr1值为null返回expr2的值，否则返回expr1的值
```
select name  
from customer
where IFNULL(referee_id,0) != 2
```
## 字符串操作
### substring
```
substring(str, start_index, length)
```
### 大小写
```
UPPER(str)
LOWER(str)
```
### concat
```
concat(str1, str2)
str1+str2
```
### group_concat
将元素组合为一个字符串
```
group_concat(distinct product) as products

group_concat(class, ':',score separator ',') as 'class:score'
```
## 日期操作
### dateDiff()
计算日期天数差
### date_sub
返回某一日期前特定天的日期
```
date_sub('2019-07-27', interval 30 day)
```
### year, month, day
提取年月日

## statistics
```
sum, count, max, min(case when)
sum, count, max, min(if )
```
## 临时表
```
WITH t AS 
(

SELECT account, SUM(amount) balance 
FROM Transactions GROUP BY account HAVING SUM(amount)>10000
)
SELECT name, balance
FROM t JOIN Users USING(account)
```

## DataFrame操作
### 行转列
把数据表中具有相同key值的多行value数据，转换为使用一个key值的多列数据，使每一行数据中，一个key对应多个value。
1. if or case when
```
select name,
	max(if(class = '数学', score, null)) as math_score,
	max(if(class = '英语', score, null)) as engilsh_score,
	max(if(class = '语文', score, null)) as chinese_score,
	max(if(class = '历史', score, null)) as history_score
from student_x
group by name;
```
2. pivot
```
SELECT *
FROM student
PIVOT (
    SUM(score) FOR subject IN (语文, 数学, 英语)
)
```
3. group_concat
```
select name,
	group_concat(class,':',score separator ',') as 'class:score'
from student_x
group by name;
```
4. 动态sql
```
set @select_columns = ''; -- 定义变量
select 
	@select_columns := concat(@select_columns,'sum(if(class= \'',
		class,'\',score,null)) as ',class, ',') as select_column -- 赋值的时候，使用concat函数连接最后的字段集合
from (
	select distinct class from student_x -- 统计去重后的科目名称集合
) as t; -- 为变量赋值
select @select_columns; -- 查看变量结果
set @select_sql := concat('select name, ', 
		substring(@select_columns, 1, char_length(@select_columns) - 1),
		' from student_x group by name;'
); -- 使用concat函数，拼装SQL语句
select @select_sql; -- 查看最后拼装的完整的SQL语句
-- 准备执行SQL语句
prepare stmt from @select_sql;
execute stmt; -- 执行SQL语句
deallocate prepare stmt; -- 释放变量资源
```
### 列转行
把表中同一个key值对应的多个value列，转换为多行数据，使每一行数据中，保证一个key只对应一个value。
1. union all
```
select * from (
	select name, 'math_score' as class, math_score as score from student_y
	union all
	select name, 'engilsh_score' as class, engilsh_score as score from student_y
	union all
	select name, 'chinese_score' as class, chinese_score as score from student_y
	union all
	select name, 'history_score' as class, history_score as score from student_y
) as x order by name,class;

```
2. unpivot
```
SELECT *
FROM student1
UNPIVOT (
    score FOR subject IN ("语文","数学","英语")
)
```
3. 使用substring_index解析group_concat结构
```
select 
	x.name,
	substring_index(substring_index(x.scores, ',', y.help_topic_id + 1), ',', -1) as 'score'
from student_y2 as x
join mysql.help_topic y
on y.help_topic_id < (length(x.scores) - length(replace(x.scores, ',', '')) + 1);
```


