create database dataanalytics;
use dataanalytics;
create table persons(
pid int,
lname varchar(255),
fname varchar(255),
address varchar(255),
city varchar(255));
insert into persons values(1,'rahool','chandra','vizag',
'vishaka');
insert into persons values(2,'basha','shiek','godari',
'west');
insert into persons values(3,'vishnu','vardhan','vijaywada',
'bezawada');
select * from persons;
SET SQL_SAFE_UPDATES = 0;
delete from persons where pid=2;
update persons set fname='Rahoool' where pid=1;

create table users(
uid int auto_increment primary key,
uname varchar(50) unique not null,
email varchar(100) unique not null,
fname varchar(50),
lname varchar(50),
dob date,
createdat datetime default current_timestamp,
lastlogin datetime,
status enum('active','inactive','suspended'),
index (Email)
);
alter table users  add passwords varchar(50);
delete from users where uid=1;
select * from users;
insert into users values(1,'rahool','rahl@gmail.com','rahl','ram','2002-02-02',now(),now(),'active','rahool@20');

create table students(
sid int primary key,
name varchar(30),
age int check(age>18)
);
insert into students values(1,'vishnu',21);
 insert into students values(2,'basha',22);
 insert into students values(3,'rahul',20);
 select * from students; 
create table enrollment(
enrolId int,
sid int,
courseid int,
foreign key (sid) references students(sid)
);
insert into enrollment values(101,1,501);
insert into enrollment values(102,2,502);
insert into enrollment values(103,3,501);
select *from enrollment;


create table orderdetails(
order_id int,
product_id int,
quantity int,
primary key(order_id,product_id)
);
insert into orderdetails values(1,101,5000);
insert into orderdetails values(1,103,5000);
insert into orderdetails values(2,101,5000);
select * from orderdetails;
truncate table orderdetails;
drop table orderdetails;


