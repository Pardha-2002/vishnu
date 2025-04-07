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
