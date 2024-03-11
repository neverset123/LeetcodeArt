/*
创建数据库
创建临时表
STRIGN不支持所有的数据库，因此需要使用VARCHAR 
*/
CREATE DATABASE IF NOT EXISTS test;
CREATE TABLE IF NOT EXISTS test.t (c1 INT PRIMARY KEY, c2 STRING NOT NULL UNIQUE); /* constraint t non null and unique in table*/
CREATE TABLE IF NOT EXISTS test.t (c1 INT, c2 STRING, PRIMARY KEY(c1, c2)); /* composite key to guarantee uniqueness*/
CREATE TABLE IF NOT EXISTS test.t (c1 INT, c2 STRING, PRIMARY KEY((c1),c2)); /* primary key made up of partition key and clustering key in cassandra*/
CREATE TABLE IF NOT EXISTS test.t (c1 INT REFERENCES t1(c1), c2 STRING, PRIMARY KEY(c1, c2)); /* foreign key reference*/
CREATE EXTERNAL TABLE IF NOT EXISTS test.t (c1 INT, c2 STRING) LOCATION '/path/to/data'; /* external table*/
ALTER TABLE test.t ADD COLUMNS (c3 INT);
ALTER TABLE test.t Modify COLUMN c3 STRING;
INSERT INTO test.t VALUES (1, 'a'), (2, 'b'), (3, 'c');
INSERT INTO test.t (c1, c2) VALUES (1, 'a'), (2, 'b'), (3, 'c') ;
INSERT INTO test.t SELECT * FROM test.t WHERE c = 'a'; 
INSERT INTO test.t (c1, c2) VALUES (1,'a') ON CONFLICT (c1) DO UPDATE SET c2 = 'a'; -- 如果主键冲突，则更新
INSERT INTO test.t (c1, c2) SELECT * FROM test.t WHERE c = 'a' ON CONFLICT (c1) DO NOTHING;
UPDATE test.t SET c = 'd' WHERE c = 'a';
UPDATE test.t SET c =(IF(c = 'a', 'd', 'e'));
DELETE FROM test.t WHERE c = 'a';
DELETE t1 FROM test.t t1, test.t t2 WHERE t1.c1 = t2.c1 AND t1.id > t2.id; -- 删除重复行
DROP DATABASE IF EXISTS test;
DROP TABLE IF EXISTS test.t;

COPY test.t FROM '/path/to/file.csv' WITH csv; -- 从文件中导入数据

WITH t1 AS (SELECT * FROM t WHERE c1 = 1), t2 AS (SELECT * FROM t WHERE c1 = 2) 
SELECT * FROM t1 UNION ALL SELECT * FROM t2;

--创建external table
CREATE EXTENSION IF NOT EXISTS file_fdw;
CREATE SERVER csv_files FOREIGN DATA WRAPPER file_fdw;
CREATE FOREIGN TABLE my_external_table (
    column1 INT,
    column2 VARCHAR(255),
    column3 DATE
)
SERVER csv_files
OPTIONS (format 'csv', filename '/path/to/your/file.csv', delimiter ',', header 'true');

/*
随机抽样：TABLESAMPLE BERNOULLI(10) 表示随机抽取10%的数据
RAND()：返回一个0到1之间的随机数
*/
SELECT * FROM t TABLESAMPLE BERNOULLI(10);
SELECT * FROM t WHERE RAND() < 0.1; -- 随机抽取10%的数据

/*
动态sql
*/
SET @sql = 'SELECT * FROM t';   -- 动态sql
select @sql;                -- 打印sql
PREPARE stmt FROM @sql;    -- 预编译sql
EXECUTE stmt;           -- 执行sql
DEALLOCATE PREPARE stmt;    -- 释放sql


/*
模糊查询：%表示任意多个字符，_表示任意单个字符， []表示括号内的任意单个字符，[^]表示括号内的任意单个字符之外的字符，
starting with：以...开头
百分位查询：PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY c) 表示中位数
*/
SELECT * FROM t WHERE c LIKE '%a%';
SELECT * FROM t WHERE c LIKE '_a%';
SELECT * FROM t WHERE c LIKE '[abc]%';
SELECT * FROM t WHERE c LIKE '[^abc]%';
SELECT * FROM t WHERE c starting with 'a';
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY c) FROM t;

/*
字段处理
EXTRACT：提取日期中的年、月、日、时、分、秒、星期，季度等
DATEDIFF：计算两个日期的差，参数2-参数1
DATESUB：日期减去一个时间间隔，参数1-参数2
DATEADD：日期加上一个时间间隔，参数1+参数2
CONCAT：连接字符串（或者用+代替）
CONCAT_WS：连接字符串，第一个参数为分隔符
Group_concat：将多列合并成一列，或多行合并成一行
LENGTH：返回字符串长度
LOWER：转换为小写
UPPER：转换为大写
TRIM：去除首尾空格
LTRIM：去除首部空格
RTRIM：去除尾部空格
REPLACE：替换字符串
SUBSTRING：截取字符串
SUBSTRING_INDEX：截取字符串，第三个参数为第几次出现的分隔符
*/
SELECT EXTRACT(YEAR FROM c) FROM t;
SELECT EXTRACT(ISODOW FROM c) FROM t; -- 1-7表示周一到周日
SELECT DATEDIFF(MINUTE, '2019-01-01', '2019-01-02') FROM t;
SELECT DATESUB('2019-01-01', INTERVAL 1 DAY) FROM t;
SELECT DATEADD('2019-01-01', INTERVAL 1 DAY) FROM t;

SELECT CONCAT(c1, c2) FROM t; -- 如果有NULL，则返回NULL 
SELECT CONCAT_WS(',', c1, c2) FROM t; -- 如果有NULL，则忽略NULL
SELECT c1+c2 FROM t; -- 如果有NULL，则返回NULL
SELECT GROUP_CONCAT(c1, ":", c2 SEPARATOR ',') AS "c1:c2" FROM t; 
SELECT LENGTH(c) FROM t;
SELECT LOWER(c) FROM t;
SELECT UPPER(c) FROM t;
SELECT TRIM(c) FROM t;
SELECT LTRIM(c) FROM t;
SELECT RTRIM(c) FROM t;
SELECT REPLACE(c, 'a', 'b') FROM t;
SELECT SUBSTRING(c, 1, 2) FROM t; -- 从第1个字符开始截取2个字符
SELECT SUBSTRING_INDEX(c, ',', 1) FROM t; -- 从左往右截取第1次出现的逗号之前的字符串
SELECT c1 FROM t WHERE mod(id, 2) = 0; -- 取偶数行

/*
IF条件判断：IF(条件, 结果1, 结果2)
IFNULL：如果第一个参数不是 NULL，则返回第一个参数，否则返回第二个参数
ISNULL：如果第一个参数为 NULL，则返回 1，否则返回 0
CASE条件判断：  CASE WHEN 条件1 THEN 结果1 WHEN 条件2 THEN 结果2 ELSE 结果3 END
*/
SELECT IF(c = 1, 'one', 'other') FROM t;
SELECT SUM(IF(c = 1, 1, 0)) FROM t;
SELECT IFNULL(c, 0) FROM t; -- 等价于 IF(c IS NULL, 0, c)
SELECT ISNULL(c) FROM t; -- 等价于 c IS NULL, 如果c为NULL，则返回1，否则返回0
SELECT CASE WHEN c = 1 THEN 'one' WHEN c = 2 THEN 'two' ELSE 'other' END FROM t;

/*
排序：ORDER BY c1 [ASC|DESC]，默认升序
分组排序：row_number()
*/
SELECT * FROM t ORDER BY c1 limit 1 offset 1; -- limit表示取多少行，offset表示从第几行开始取
SELECT row_number() over (partition by c1 order by c2) as rn FROM t;

/*
比较运算符：=、<>、!=、<、<=、>、>=、<=>、BETWEEN、IS NULL、IS NOT NULL、IN、NOT IN、LIKE、REGEXP、RLIKE、ANY、SOME、ALL
逻辑运算符：AND、&&、OR、||、NOT、!

*/
SELECT * FROM t WHERE c1 BETWEEN 1 AND 2;
SELECT * FROM t WHERE c1 IS NULL;   -- 等价于 ISNULL
SELECT * FROM t WHERE c1 IS NOT NULL;
SELECT * FROM t WHERE c1 IN (1, 2);
SELECT * FROM t WHERE c1 NOT IN (1, 2);
SELECT * FROM t WHERE c1 LIKE '%a%';
SELECT * FROM t WHERE c1 REGEXP 'a'; -- 等价于 RLIKE, 表示匹配正则表达式
SELECT * FROM t WHERE c1 RLIKE 'a'; -- 等价于 REGEXP
SELECT * FROM t WHERE column_name > ANY (SELECT column_name FROM table_name WHERE condition); --在sql中，ANY和SOME是等价的
SELECT * FROM t WHERE column_name > SOME (SELECT column_name FROM table_name WHERE condition);
SELECT * FROM t WHERE column_name > ALL (SELECT column_name FROM table_name WHERE condition);
SELECT * FROM t WHERE c1 AND c2;
SELECT * FROM t WHERE c1 OR c2;
SELECT * FROM t WHERE NOT c1;
SELECT * FROM t WHERE !c1;

/*
聚合函数：AVG、COUNT、MAX、MIN、SUM
窗口函数：ROW_NUMBER、RANK、DENSE_RANK、PERCENT_RANK、CUME_DIST、NTILE、LAG、LEAD、FIRST_VALUE、LAST_VALUE, PARTITION BY

*/
SELECT AVG(c) FROM t;
SELECT COUNT(c) FROM t;
SELECT MAX(c) FROM t;
SELECT MIN(c) FROM t;
SELECT SUM(c) FROM t;

SELECT ROW_NUMBER() OVER (ORDER BY c) FROM t; -- 从1开始的连续整数
SELECT RANK() OVER (ORDER BY c) FROM t; -- 不连续有重复编号，相同的值排名相同，下一个值跳过相同的排名
SELECT DENSE_RANK() OVER (ORDER BY c) FROM t; -- 持续有重复编号
SELECT PERCENT_RANK() OVER (ORDER BY c) FROM t;
SELECT CUME_DIST() OVER (ORDER BY c) FROM t;
SELECT NTILE(2) OVER (ORDER BY c) FROM t;
SELECT LAG(c) OVER (ORDER BY c) FROM t;
SELECT LEAD(c) OVER (ORDER BY c) FROM t;
SELECT FIRST_VALUE(c) OVER (ORDER BY c) FROM t;
SELECT LAST_VALUE(c) OVER (ORDER BY c) FROM t;

/* 
分组查询 
*/
SELECT c1, COUNT(*) FROM t GROUP BY c1; -- c1 可以是case when结构
SELECT c1, SUM(c2) FROM t GROUP BY c1; -- c2 可以是case when结构
SELECT c1, c2, COUNT(*) FROM t GROUP BY c1, c2;

/*
关联查询
*/
SELECT * FROM t1, t2 WHERE t1.c1 = t2.c1;
SELECT * FROM t1 WHERE t1.c1 = (SELECT min(c1) FROM t2 WHERE t1.c2 = t2.c2);
SELECT * FROM t1 WHERE (c1, c2)  in (SELECT min(c1), c2 FROM t2 GROUP BY c2);

/*
跨表查询
Union：合并两个或多个 SELECT 语句的结果集，去除重复行
Union All：合并两个或多个 SELECT 语句的结果集，不去除重复行
Intersect：交集
Except：差集
Minus：差集
inner join：内连接, default join
left join：左连接
right join：右连接
full join：全连接
cross join：笛卡尔积
*/
SELECT * FROM t1 UNION SELECT * FROM t2;
SELECT * FROM t1 UNION ALL SELECT * FROM t2;
SELECT * FROM t1 INTERSECT SELECT * FROM t2;
SELECT * FROM t1 EXCEPT SELECT * FROM t2;
SELECT * FROM t1 MINUS SELECT * FROM t2;
SELECT * FROM t1 INNER JOIN t2 ON t1.c1 = t2.c1; /* avoid select * to avoid duplicating the joined key in result */
SELECT * FROM t1 LEFT JOIN t2 using (c1); /* using表示两个表中的列名相同 */


/*
嵌套查询
*/
SELECT * FROM t WHERE EXISTS (SELECT * FROM t2 WHERE t.c1 = t2.c1);
SELECT * FROM t WHERE c1 IN (SELECT c1 FROM t2 WHERE t.c2 = t2.c2);
SELECT * FROM t WHERE c1 IN (SELECT c1 FROM t2 GROUP BY c1 HAVING COUNT(*) > 1);

/*
行转列，把数据表中具有相同key值的多行value数据，转换为使用一个key值的多列数据，使每一行数据中，一个key对应多个value。
列转行，把数据表中的多列数据，转换为使用一个key值的多行数据，使每一行数据中，一个key对应一个value。
*/
SELECT c1, MAX(IF(c2 = 'a', c3, NULL)) AS a, MAX(IF(c2 = 'b', c3, NULL)) AS b FROM t GROUP BY c1;
SELECT * from t pivot (max(c3) for c2 in ('a', 'b')) as p; -- 等价于上面的写法


SELECT c1, c2, c3 FROM t UNPIVOT (c3 FOR c2 IN ('a', 'b')) AS p; -- 等价于上面的写法
SELECT 'a' AS c2, a AS c3 FROM t UNION ALL SELECT 'b' AS c2, b AS c3 FROM t;


