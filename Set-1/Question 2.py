"""
Write Sql command for the queries (i) to (v) based on the table COMPANY and Customer.

1) To display those company name along along with price which are having less than 30000.
2) To display the name and price of the companies whose price is between 20000 and 35000.
3) To increase the price by 1000 for those customers whose name starts with 'S'.
4) To display the product name, city and price which are having product name as MOBILE.
"""

# COMPANY
"""
CID     CNAME       CITY    PRODUCTNAME
111     SONY        DELHI   TV
222     NOKIA       MUMBAI  MOBILE
333     ONIDA       DELHI   TV
444     SONY        MUMBAI  MOBILE
555     BLACKBERRY  MADRAS  MOBILE
666     DELL        DELHI   LAPTOP
"""

# CUSTOMER
"""
CUSTID  NAME            PRICE   QTY    CID
101     Rohan Sharma    70000   20     222
102     Deepak Kumar    50000   10     666
103     Mohan Kumar     30000   5      111
104     Sahil Bansal    35000   3      333
105     Neha Soni       25000   7      444
106     Sonal Aggarwal  20000   5      333
107     Arjun Singh     50000   15     666
"""
"""
create table company(cid integer primary key, cname varchar(30), city varchar(30), pname varchar(30));

insert into company values(111, "sony", "delhi", "tv"); 
insert into company values(222, "nokia", "mumbai", "mobile");
insert into company values(333, "onida", "delhi", "tv")
insert into company values(444, "sony", "mumbai", "mobile");
insert into company values(555, "blackberry", "madras", "mobile");
insert into company values(666, "dell", "delhi", "laptop");
"""
# 1) To display those company name along with price which are having less than 30000.
query1 = """
SELECT COMPANY.CNAME, CUSTOMER.PRICE
FROM COMPANY
JOIN CUSTOMER ON COMPANY.CID = CUSTOMER.CID
WHERE CUSTOMER.PRICE < 30000;
"""

# 2) To display the name and price of the companies whose price is between 20000 and 35000.
query2 = """
SELECT COMPANY.CNAME, CUSTOMER.PRICE
FROM COMPANY
JOIN CUSTOMER ON COMPANY.CID = CUSTOMER.CID
WHERE CUSTOMER.PRICE BETWEEN 20000 AND 35000;
"""

# 3) To increase the price by 1000 for those customers whose name starts with 'S'.
query3 = """
UPDATE CUSTOMER
SET PRICE = PRICE + 1000
WHERE NAME LIKE 'S%';
"""

# 4) To display the product name, city and price which are having product name as MOBILE.
query4 = """
SELECT COMPANY.PRODUCTNAME, COMPANY.CITY, CUSTOMER.PRICE
FROM COMPANY
JOIN CUSTOMER ON COMPANY.CID = CUSTOMER.CID
WHERE COMPANY.PRODUCTNAME = 'MOBILE';
"""



import mysql.connector

# COMPANY
"""
CID     CNAME       CITY    PRODUCTNAME
111     SONY        DELHI   TV
222     NOKIA       MUMBAI  MOBILE
333     ONIDA       DELHI   TV
444     SONY        MUMBAI  MOBILE
555     BLACKBERRY  MADRAS  MOBILE
666     DELL        DELHI   LAPTOP
"""
"""
# Connect to MySQL
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

# Create table
create_table_query = """
CREATE TABLE COMPANY (
    CID INT PRIMARY KEY,
    CNAME VARCHAR(50),
    CITY VARCHAR(50),
    PRODUCTNAME VARCHAR(50)
);
"""
cursor.execute(create_table_query)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
"""
