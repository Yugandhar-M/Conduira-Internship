Answers are written in MySQL
## Question 1
Creating and Inserting data into tables.
```
CREATE TABLE EmployeesTable(
    EMP_ID INT NOT NULL,
    FIRST_NAME CHAR(50),
    LAST_NAME CHAR(50),
    SALARY INT,
    JOINING_DATE DATETIME,
    DEPARTMENT CHAR(10)
    );
INSERT INTO EmployeesTable VALUES
    (001,"Manish","Agrawal",700000,"2019-04-20 09:00:00","HR"),
	(002,"Niranjan","Bose",20000,"2019-02-11 09:00:00","DA"),
	(003,"Vivek","Singh",100000,"2019-01-20 09:00:00","DA"),
	(004,"Asutosh","Kapoor",700000,"2019-03-20 09:00:00","HR"),
	(005,"Vihaan","Banerjee",300000,"2019-06-11 09:00:00","DA"),
	(006,"Atul","Diwedi",400000,"2019-05-11 09:00:00","Account"),
	(007,"Satyendra","Tripathi",95000,"2019-03-20 09:00:00","Account"),
	(008,"Pritika","Bhatt",80000,"2019-02-11 09:00:00","DA");
CREATE TABLE VariablesDetails(EMP_REF_ID INT NOT NULL, VARIABLES_DATE DATETIME, VARIABLES_AMOUNT INT);
INSERT INTO VariablesDetails VALUES
    (1,"2019-02-20 00:00:00",15000),
	(2,"2019-06-11 00:00:00",30000),
    (3,"2019-02-20 00:00:00",42000),
    (4,"2019-02-20 00:00:00",14500),
    (5,"2019-06-11 00:00:00",23500);
CREATE TABLE DesignationTable(EMP_REF_ID INT NOT NULL, EMP_TITLE CHAR(30), AFFECTED_FROM DATETIME);
INSERT INTO DesignationTable VALUES
    (1,"Asst. Manager","2019-02-20 00:00:00"),
	(2,"Senior Analyst","2019-01-11 00:00:00"),
    (8,"Senior Analyst","2019-04-06 00:00:00"),
    (5,"Manager","2019-10-06 00:00:00"),
    (4,"Asst. Manager","2019-12-06 00:00:00"),
    (7,"Team Lead","2019-06-06 00:00:00"),
    (6,"Team Lead","2019-09-06 00:00:00"),
    (3,"Senior Analyst","2019-08-06 00:00:00");
```
a. Adding Primary Key(EMP_ID) Constraint to 'EmployeesTable'.
 Constraints used are EMP_ID column cannot have a null value.
```    
ALTER TABLE EmployeesTable ADD CONSTRAINT PRIMARY KEY (EMP_ID);
```
b. Adding Foreign Key(EMP_REF_ID) Constraints to 'VariablesDetails' and 'DesignationTable'
```
ALTER TABLE VariablesDetails ADD CONSTRAINT FOREIGN KEY (EMP_REF_ID) REFERENCES EMPLOYEESTABLE (EMP_ID);
ALTER TABLE DesignationTable ADD CONSTRAINT FOREIGN KEY (EMP_REF_ID) REFERENCES EMPLOYEESTABLE (EMP_ID);
```

## Question 2
<pre>
INNER JOIN:
&nbsp;  Joins two tables with reference to a common column specified. And stores only that data for which the common column specified matches.
LEFT JOIN:
&nbsp;  Joins two tables with reference to a common column specified. Takes all data from table on left but only matched data from table on right.
RIGHT JOIN:
&nbsp;  Joins two tables with reference to a common column specified. Takes all data from table on right but only matched data from table on left.
CROSS JOIN:
&nbsp;  Joins two tables. Returns all possible combinations of mapping of data from both tables.
</pre>
Queries demonstrating JOIN Operations:<br>
CROSS JOIN
```
SELECT CONCAT(FIRST_NAME," ",LAST_NAME) AS "FULL NAME", EMP_TITLE 
    FROM employeestable 
    CROSS JOIN designationtable 
    ORDER BY FIRST_NAME;
```
LEFT JOIN
```
SELECT CONCAT(FIRST_NAME," ",LAST_NAME) AS "FULL NAME", EMP_TITLE 
    FROM employeestable AS E 
    LEFT JOIN designationtable AS D ON E.EMP_ID=D.EMP_REF_ID 
    ORDER BY FIRST_NAME;
```
RIGHT JOIN
```
SELECT CONCAT(FIRST_NAME," ",LAST_NAME) AS "FULL NAME", EMP_TITLE 
    FROM designationtable AS D 
    RIGHT JOIN employeestable AS E 
    ON E.EMP_ID=D.EMP_REF_ID 
    ORDER BY FIRST_NAME;
```
INNER JOIN
```
SELECT CONCAT(FIRST_NAME," ",LAST_NAME) AS "FULL NAME", EMP_TITLE 
    FROM designationtable AS D 
    INNER JOIN employeestable AS E 
    ON E.EMP_ID=D.EMP_REF_ID 
    ORDER BY FIRST_NAME;
```


a. Query to get Employee details(Full Name, Department) of those who received highest and least variables.
```
SELECT CONCAT(E.FIRST_NAME," ",E.LAST_NAME) AS "Full Name", E.Department 
FROM EmployeesTable AS E RIGHT JOIN VariablesDetails AS V ON E.EMP_ID=V.EMP_REF_ID 
WHERE 
    V.VARIABLES_AMOUNT = (SELECT MAX(VARIABLES_AMOUNT) FROM VariablesDetails) 
OR 
    V.VARIABLES_AMOUNT = (SELECT MIN(VARIABLES_AMOUNT) FROM  VariablesDetails);
```


b. Query to get designations which got higest and second lowest amount of (salary + variables)
```
SELECT EMP_TITLE, AMOUNT 
FROM 
	(SELECT EMP_TITLE, (IFNULL(VARIABLES_AMOUNT,0)+SALARY) AS AMOUNT 
    FROM EmployeesTable E 
	INNER JOIN DesignationTable D ON E.EMP_ID=D.EMP_REF_ID 
    LEFT OUTER JOIN VariablesDetails V ON V.EMP_REF_ID=D.EMP_REF_ID) AS ONE
WHERE 
	AMOUNT=(SELECT MAX(AMOUNT) FROM 
    (SELECT EMP_TITLE, (IFNULL(VARIABLES_AMOUNT,0)+SALARY) AS AMOUNT 
    FROM EmployeesTable E 
	INNER JOIN DesignationTable D ON E.emp_id=D.EMP_REF_ID 
    LEFT OUTER JOIN VariablesDetails V ON V.EMP_REF_ID=D.EMP_REF_ID) AS TWO) 
OR
	AMOUNT=(SELECT MIN(AMOUNT) FROM 
    (SELECT EMP_TITLE, (IFNULL(VARIABLES_AMOUNT,0)+SALARY) AS AMOUNT 
    FROM EmployeesTable E 
	INNER JOIN DesignationTable D ON E.emp_id=D.EMP_REF_ID 
    LEFT OUTER JOIN VariablesDetails V ON V.EMP_REF_ID=D.EMP_REF_ID) AS THREE 
	WHERE 
		AMOUNT > 
        (SELECT MIN( AMOUNT )FROM 
        (SELECT EMP_TITLE, (IFNULL(VARIABLES_AMOUNT,0)+SALARY) AS AMOUNT 
        FROM EmployeesTable E 
		INNER JOIN DesignationTable D ON E.EMP_ID=D.EMP_REF_ID 
        LEFT OUTER JOIN VariablesDetails V ON V.EMP_REF_ID=D.EMP_REF_ID) AS FOUR));
```
c. Cross Join: <br>Mapping all rows of one table to all rows of other table. This is similar to cartesian product in sets where each element is like a row in table.<br>
The following query outputs all possible combinations of (names:designations) pairs.
```
SELECT CONCAT(FIRST_NAME," ",LAST_NAME) AS "FULL NAME", EMP_TITLE 
FROM employeestable 
CROSS JOIN designationtable 
ORDER BY FIRST_NAME;
```
d. Clauses with SELECT Statement
<pre>Preference Order: DISTINCT, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT
WHERE Clause:
&nbsp;  This is used for conditional retrieval of data.
ORDER BY Clause:
&nbsp;  This is used for ordered display of resutls by sorting them.
LIMIT Clause:
&nbsp;  Used to limit the number of rows getting displayed.
DISTINCT Clause:
&nbsp;  For obtaining distinct values when querying.
GROUP BY Clause:
&nbsp;  For grouping data based on some common properties.
HAVING Clause:
&nbsp;  It is also used to put some conditions in data retreival. But used with GROUP BY Clause and can only be used on column that is listed in SELECT Statement.</pre>

## Question 3
<u>Stored Procedure:</u>
<br>Method to store set of SQL statements which can be used later invoking it by its name. 
<br><br>
a. Query to return Employee details whose designations got updated in second half of 2019 sorted by 'Variables_Amount' from high to low.
``` 
SELECT E.EMP_ID, CONCAT(E.FIRST_NAME," ",E.LAST_NAME) AS "Full Name", E.Department 
FROM EmployeesTable AS E
LEFT JOIN Variablesdetails AS V
	ON E.EMP_ID=V.EMP_REF_ID 
LEFT JOIN designationtable AS D
	ON E.EMP_ID=D.EMP_REF_ID
WHERE 
    (MONTH(D.AFFECTED_FROM) BETWEEN 7 AND 12) AND (YEAR(D.AFFECTED_FROM)=2019)
ORDER BY 
    V.VARIABLES_AMOUNT DESC;
```
b. Query to create and call a procedure in MySQL. The query within procedure is from Q2.a
```
DELIMITER $$
CREATE PROCEDURE GetEmployees()
BEGIN
    SELECT CONCAT(E.FIRST_NAME," ",E.LAST_NAME) AS "Full Name", E.Department 
	FROM EmployeesTable AS E RIGHT JOIN VariablesDetails AS V ON E.EMP_ID=V.EMP_REF_ID 
	WHERE V.VARIABLES_AMOUNT = (SELECT MAX(VARIABLES_AMOUNT) FROM VariablesDetails) 
	OR V.VARIABLES_AMOUNT = (SELECT MIN(VARIABLES_AMOUNT) FROM  VariablesDetails);
END$$
DELIMITER ;

CALL GetEmployees();
```

