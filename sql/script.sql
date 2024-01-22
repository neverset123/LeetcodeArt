/*
创建数据库
*/
CREATE DATABASE IF NOT EXISTS test;
CREATE TABLE IF NOT EXISTS test.t (c1 INT, c2 STRING);
ALTER TABLE test.t ADD COLUMNS (c3 INT);
ALTER TABLE test.t Modify COLUMN c3 STRING;
INSERT INTO test.t VALUES (1, 'a'), (2, 'b'), (3, 'c');
INSERT INTO test.t SELECT * FROM test.t WHERE c = 'a';
UPDATE test.t SET c = 'd' WHERE c = 'a';
DELETE FROM test.t WHERE c = 'a';
DROP DATABASE IF EXISTS test;

/*
随机抽样：TABLESAMPLE BERNOULLI(10) 表示随机抽取10%的数据
RAND()：返回一个0到1之间的随机数
*/
SELECT * FROM t TABLESAMPLE BERNOULLI(10);
SELECT * FROM t WHERE RAND() < 0.1;

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
EXTRACT：提取日期中的年、月、日、时、分、秒
CONCAT：连接字符串
CONCAT_WS：连接字符串，第一个参数为分隔符
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
SELECT CONCAT(c1, c2) FROM t;
SELECT CONCAT_WS(',', c1, c2) FROM t;
SELECT LENGTH(c) FROM t;
SELECT LOWER(c) FROM t;
SELECT UPPER(c) FROM t;
SELECT TRIM(c) FROM t;
SELECT LTRIM(c) FROM t;
SELECT RTRIM(c) FROM t;
SELECT REPLACE(c, 'a', 'b') FROM t;
SELECT SUBSTRING(c, 1, 2) FROM t;
SELECT SUBSTRING_INDEX(c, ',', 1) FROM t;

/*
IF条件判断：IF(条件, 结果1, 结果2)
IFNULL：如果第一个参数不是 NULL，则返回第一个参数，否则返回第二个参数
ISNULL：如果第一个参数为 NULL，则返回 1，否则返回 0
*/
SELECT IF(c = 1, 'one', 'other') FROM t;
SELECT SUM(IF(c = 1, 1, 0)) FROM t;
SELECT IFNULL(c, 0) FROM t;
SELECT ISNULL(c) FROM t;

/*
CASE条件判断：  CASE WHEN 条件1 THEN 结果1 WHEN 条件2 THEN 结果2 ELSE 结果3 END
*/
SELECT CASE WHEN c = 1 THEN 'one' WHEN c = 2 THEN 'two' ELSE 'other' END FROM t;

/*
排序：ORDER BY c1 [ASC|DESC]，默认升序
分组排序：row_number()
*/
SELECT row_number() over (partition by c1 order by c2) as rn FROM t;

/*
比较运算符：=、<>、!=、<、<=、>、>=、<=>、BETWEEN、IS NULL、IS NOT NULL、IN、NOT IN、LIKE、REGEXP、RLIKE、ANY、SOME、ALL
逻辑运算符：AND、&&、OR、||、NOT、!

*/
SELECT * FROM t WHERE c1 BETWEEN 1 AND 2;
SELECT * FROM t WHERE c1 IS NULL;
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
窗口函数：ROW_NUMBER、RANK、DENSE_RANK、PERCENT_RANK、CUME_DIST、NTILE、LAG、LEAD、FIRST_VALUE、LAST_VALUE

*/
SELECT AVG(c) FROM t;
SELECT COUNT(c) FROM t;
SELECT MAX(c) FROM t;
SELECT MIN(c) FROM t;
SELECT SUM(c) FROM t;

SELECT ROW_NUMBER() OVER (ORDER BY c) FROM t; -- 从1开始的连续整数
SELECT RANK() OVER (ORDER BY c) FROM t; -- 并列第一名，下一个名次跳过
SELECT DENSE_RANK() OVER (ORDER BY c) FROM t; -- 并列第一名，下一个名次不跳过
SELECT PERCENT_RANK() OVER (ORDER BY c) FROM t;
SELECT CUME_DIST() OVER (ORDER BY c) FROM t;
SELECT NTILE(2) OVER (ORDER BY c) FROM t;
SELECT LAG(c) OVER (ORDER BY c) FROM t;
SELECT LEAD(c) OVER (ORDER BY c) FROM t;
SELECT FIRST_VALUE(c) OVER (ORDER BY c) FROM t;
SELECT LAST_VALUE(c) OVER (ORDER BY c) FROM t;


/*
多表查询
Union：合并两个或多个 SELECT 语句的结果集，去除重复行
Union All：合并两个或多个 SELECT 语句的结果集，不去除重复行
Intersect：交集
Except：差集
Minus：差集
*/
SELECT * FROM t1 UNION SELECT * FROM t2;
SELECT * FROM t1 UNION ALL SELECT * FROM t2;
SELECT * FROM t1 INTERSECT SELECT * FROM t2;
SELECT * FROM t1 EXCEPT SELECT * FROM t2;
SELECT * FROM t1 MINUS SELECT * FROM t2;

