-- 문제1
SELECT
	employeeNumber,
    lastName,
    firstName,
    city
FROM
	employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

-- 문제2
SELECT
	customerNumber,
    officeCode,
    customers.city,
    offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제3
SELECT
	customerNumber,
    officeCode,
    customers.city,
    offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제4
SELECT
	customerNumber,
    officeCode,
    customers.city,
    offices.city
FROM
	customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제5
-- 문제 2는 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드를 반환한다.
-- 문제 3은 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드를 반환한다.
-- 문제 4는 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환한다.

-- 문제6
SELECT
	customerNumber,
    officeCode,
    customers.city,
    offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT
	customerNumber,
    officeCode,
    customers.city,
    offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제7
SELECT
	orderdetails.orderNumber,
    orderDate
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;

-- 문제8
SELECT
	orderNumber,
    orderdetails.productCode,
    productName
FROM
	orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;

-- 문제9
SELECT
	orderdetails.orderNumber,
    orderdetails.productCode,
    orderDate,
    productName
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;