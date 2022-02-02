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
INSERT INTO EmployeesTable VALUES(001,"Manish","Agrawal",700000,"2019-04-20 09:00:00","HR"),
	(002,"Niranjan","Bose",20000,"2019-02-11 09:00:00","DA"),
	(003,"Vivek","Singh",100000,"2019-01-20 09:00:00","DA"),
	(004,"Asutosh","Kapoor",700000,"2019-03-20 09:00:00","HR"),
	(005,"Vihaan","Banerjee",300000,"2019-06-11 09:00:00","DA"),
	(006,"Atul","Diwedi",400000,"2019-05-11 09:00:00","Account"),
	(007,"Satyendra","Tripathi",95000,"2019-03-20 09:00:00","Account"),
	(008,"Pritika","Bhatt",80000,"2019-02-11 09:00:00","DA");
CREATE TABLE VariablesDetails(EMP_REF_ID INT NOT NULL, VARIABLES_DATE DATETIME, VARIABLES_AMOUNT INT);
INSERT INTO VariablesDetails VALUES(1,"2019-02-20 00:00:00",15000),
	(2,"2019-06-11 00:00:00",30000),
    (3,"2019-02-20 00:00:00",42000),
    (4,"2019-02-20 00:00:00",14500),
    (5,"2019-06-11 00:00:00",23500);
CREATE TABLE DesignationTable(EMP_REF_ID INT NOT NULL, EMP_TITLE CHAR(30), AFFECTED_FROM DATETIME);
INSERT INTO DesignationTable VALUES(1,"Asst. Manager","2019-02-20 00:00:00"),
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
a. Query to get Employee details(Full Name, Department) of those who received highest and least variables
```
SELECT CONCAT(EmployeesTable.FIRST_NAME," ",EmployeesTable.LAST_NAME) AS "Full Name", EmployeesTable.Department FROM EmployeesTable RIGHT JOIN VariablesDetails ON EmployeesTable.EMP_ID=VariablesDetails.EMP_REF_ID WHERE VariablesDetails.VARIABLES_AMOUNT = (SELECT MAX(VARIABLES_AMOUNT) FROM VariablesDetails) OR VariablesDetails.VARIABLES_AMOUNT = (SELECT MIN(VARIABLES_AMOUNT) FROM  VariablesDetails);
```

## Question 3
<u>Stored Procedure:</u>
<br>
a. Query to return Employee details whose designations got updated in second half of 2019 sorted by 'Variables_Amount' from high to low.
``` 
SELECT empt.EMP_ID, CONCAT(empt.FIRST_NAME," ",empt.LAST_NAME) AS "Full Name", empt.Department 
FROM EmployeesTable AS empt
LEFT JOIN variablesdetails AS vdt
	ON empt.EMP_ID=vdt.EMP_REF_ID 
LEFT JOIN designationtable AS dt
	ON empt.EMP_ID=dt.EMP_REF_ID
WHERE (MONTH(dt.AFFECTED_FROM) BETWEEN 7 AND 12) AND (YEAR(dt.AFFECTED_FROM)=2019)
ORDER BY vdt.VARIABLES_AMOUNT DESC;
```