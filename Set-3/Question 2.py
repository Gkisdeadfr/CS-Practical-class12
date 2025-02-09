ec"""
1) To display the name of the teacher and their designation.
2) To display the name and subjects of all female teachers.
3) To display all details of all teachers including gender and designation.
4) To display details of all HODs
"""

"""
#Teacher Table

create table teacher(code integer primary key,tname varchar(50), subject varchar(50), DOJ date, period integer, experience integer);

insert into teacher values(1001, "Ravi Shankar", "eng", "2000-03-12", 24, 10);
insert into teacher values(1009, "Priya Rai", "physics", "1998-09-03", 26, 12);
insert into teacher values(1203, "Lisa Anand", "english", "2000-09-04", 27, 5);
insert into teacher values(1045, "Yashraj", "Maths", "2000-08-24", 24, 15);
insert into teacher values(1123, "Gagan", "physics", "1999-07-16", 28, 3);
insert into teacher values(1167, "Harish B", "Chemistry", "1999-10-19", 27, 5);
insert into teacher values(1215, "Umesh", "physics", "1998-05-11", 22, 16);

#Admin Table

create table admin(code integer primary key, gender varchar(6), designation varchar(50));
insert into admin values(1001, "male", "Vice Principal");
insert into admin values(1009, "female", "coordinator");
insert into admin values(1203, "female", "coordinator");
insert into admin values(1045, "male", "HOD");
insert into admin values(1123, "male", "Senior Teacher");
insert into admin values(1215, "male", "HOD");
insert into admin values(1167, "female", "Senior Teacher");
"""
"""
#ANSWERS
i)Select tname, designation from teacher, admin group by code;
ii)Select tname, subject from teacher, admin group by code having gender= "female";
iii)Select * from teacher, admin group by code;
iv)Select * from teacher, admin group by code having designation= "HOD";
"""
