-- 문제1
SELECT
	productCode, productName, MSRP
FROM
	products
WHERE MSRP > (SELECT AVG(MSRP) FROM products)
ORDER BY
	MSRP;

-- 문제2
SELECT
	customerNumber, customerName
FROM
	customers
WHERE customerNumber IN (
	SELECT customerNumber
	FROM orders
    WHERE orderDate BETWEEN date('2003-01-06') AND date('2003-03-26')+1)
ORDER BY
	customerNumber;

-- 문제3
SELECT
	productCode, productName, productLine, MSRP
FROM
	products
WHERE
	productLine = 'Classic Cars'
    AND MSRP = (SELECT MAX(MSRP) FROM products);

-- 문제4
SELECT
	customerNumber, customerName, country
FROM
	customers
WHERE
	country = (SELECT MAX(country) FROM customers)
ORDER BY
	customerNumber;

-- 문제5
SELECT
	customerNumber, customerName, order_count
FROM (
	SELECT customerNumber, customerName, COUNT(orderNumber) AS order_count
	FROM customers
	INNER JOIN orders USING (customerNumber)
    GROUP BY customerNumber) AS mySub
ORDER BY
	order_count DESC
LIMIT 1;
	
-- 문제6
SELECT
	productCode, productName
FROM (
	SELECT *
    FROM orderdetails
    INNER JOIN orders USING (orderNumber)
    INNER JOIN products USING (productCode)
	WHERE YEAR(orderDate) = '2004') AS mySub
GROUP BY productCode
ORDER BY
	productCode DESC;