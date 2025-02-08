"""
To display all records from FACULTY table whose Hire date is more than 05-oct-2001.
To display F_ID, Fname, Cname of those faculties who charged more than 15000 as fees.
Display count of all records from COURSES table grouped by F_ID.
Display all records FACULTY table order by First Name of the faculty in descending order.
"""
"""
#Faculty Table

create table faculty(F_ID integer primary key, FNAME varchar(30), LNAME varchar(30), Hire_date date, Salary integer);

insert into faculty values(102, "Amit", "Mishra", "12-10-1998", 12000); 
insert into faculty values(103, "Nitin", "Vyas", "24-12-1994", 8000); 
insert into faculty values(104, "Rakshit", "Soni", "18-05-2001", 14000); 
insert into faculty values(105, "Rashmi", "Malhotra", "11-09-2004", 11000); 
insert into faculty values(106, "Sulekha", "Shrivastava", "05-06-2006", 10000); 
insert into faculty values(107, "Niranjan", "Kumar", "26-08-1996", 16000); 

#Courses Table

create table courses(C_ID integer primary key, F_ID integer, Cname varchar(50), Hire_date date, Fees integer);
insert into courses values(C21, 102, Grid Computing, 40000);
insert into courses values(C22, 106, System Design, 16000);
insert into courses values(C23, 104, Computer Security, 8000);
insert into courses values(C24, 106, Human Biology, 15000);
insert into courses values(C25, 102, Computer Networks, 20000);
insert into courses values(C26, 105, Visual Basic, 6000);
insert into courses values(C27, 107, Dreamweaver, 4000);
"""
