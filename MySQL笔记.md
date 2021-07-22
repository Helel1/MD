# MySQL笔记

## 一，选择语句 select



```sql
USE sql_store;

SELECT *  -- 选择所有列
FROM customers 
-- WHERE customer_id = 1
order by first_name
```

### 1.1 distinct 不重复查询

``` sql
SELECT distinct  -- 不重复查询
	state
FROM customers
```

### 1.2 WHERE子句（条件）

运算符有以下几种

- **\>**
- **\>=**
- **<**
- **<=**
- =
- !=
- <>

练习：

```sql
-- 查询今年的订单
SELECT *

FROM orders

WHERE order_date >= '2019-01-01'
```

------

#### AND OR NOT

练习

```SQL
-- 从order_items表里面，获取订单号为6的项目
-- total price > 30
SELECT *
FROM order_items
WHERE order_id = 6 AND (quantity * unit_price) > 30 
```

-----

#### IN

```sql
SELECT *
FROM customers
WHERE state IN ('VA', 'FL', 'GA')
```

练习

``` sql
-- 查询库存量为49，38，72的产品
SELECT *
FROM products
WHERE quantity_in_stock in (49, 38, 72)
```

----

#### BETWEEN

``` sql
SELECT *
FROM customers
WHERE points BETWEEN 1000 AND 3000
```

练习

```sql
-- 查询生日介于1999-01-01 -> 2000-01-01的顾客
SELECT *
FROM customers
WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01'
```

----

 #### LIKE

匹配字符串

’%‘ 代表任意数量任意字符

‘_’ 代表一个任意字符

```sql
SELECT *
FROM customers
WHERE last_name LIKE '_____y'
```

练习

```sql
-- 获取地址含有trail或avenue的顾客
-- 获取电话含号码以9结尾的顾客
SELECT *
FROM customers
WHERE address LIKE '%trail%' OR 
	  address LIKE '%avenue%' 

SELECT *
FROM customers
WHERE phone LIKE '%9'
```

----

#### REGEXP

正则

^ 表示开头

$ 表示结尾

| 多个匹配

[abc]e: ae|be|ce

[a-d]e:等同于上面

```sql
-- first name 是ELKA或AMBUR的顾客
SELECT *
FROM customers
WHERE first_name REGEXP 'elka|ambur'


-- last name 以EY或ON结尾的
SELECT *
FROM customers
WHERE last_name REGEXP 'ey$|on$'
	  
	  
-- last name 以MY开始，或包含SE
SELECT *
FROM customers
WHERE last_name REGEXP '^MY|SE'  


-- last name 包含B而且紧跟着R或U
SELECT *
FROM customers
WHERE last_name REGEXP 'B[RU]'

```

#### 获取缺失值的记录

IS NULL

IS NOT NULL

``` sql
SELECT *
FROM customers
WHERE phone IS NULL
```

练习

``` sql
-- 获取还没发货的订单
SELECT *
FROM orders
WHERE shipped_date IS NULL
```

----

#### order by

排序

```sql
SELECT *
FROM customers
ORDER BY first_name DESC -- EDSC倒序

SELECT *
FROM customers
ORDER BY state DESC, first_name DESC
```

练习

```sql
SELECT *, quantity*unit_price AS price
FROM order_items
WHERE order_id = 2
ORDER BY price DESC
```

----

#### LIMIT (总是放在最后面)

``` sql
SELECT *
FROM customers
LIMIT 6, 3
-- 8为偏移量，指跳过6条数据，3指取三条。这里取的就是7.8.9三条
```

练习

``` sql
-- 取积分前三的顾客
SELECT *
FROM customers
ORDER BY points DESC
LIMIT 3
```

#### 内连接

INNER JOIN *table name* ON key=key

练习

```sql
SELECT order_id, oi.product_id, quantity, oi.unit_price
FROM order_items oi
INNER JOIN products p
	ON oi.product_id = p.product_id
```

----

#### 跨数据库链接



