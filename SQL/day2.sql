use dataanalytics;
create table products(pid int, pname varchar(20), price int);
insert into products values
(1,'bike',100000),
(2,'car',2000000);
insert into products values(2,'airplane',600000); 
select min(price) from products;
select min(price) as smallestprice, pid from products
group by pid;
select max(price) as smallestprice, pid from products
group by pid;
select avg(price) as smallestprice, pid from products
group by pid;

select count(*) as numberofcolumns
from products;
select count(pid) from products where price >200000;
select count(distinct pid) from products;
-- select sum(price),pname from products group by pname;
create table customer(
cid int primary key,
name varchar(20)
);
create table orders(
oid int primary key,
customer_id int,
product varchar(30),
foreign key (customer_id) references customer(cid)
on delete cascade
);
insert into customer values(1,'vishnu'),(2,'rahool'),(3,'basha');
insert into orders values(101,1,'oppo'),(102,2,'iphone'),(103,3,'onepluse');
select * from customer;
select * from orders;
delete from customer where cid=1;
create table table1(
cid int primary key,
name varchar(20)
);
create table table2(
oid int primary key,
customer_id int,
product varchar(30),
foreign key (customer_id) references table1(cid)
on update cascade
);
-- drop table table2;
insert into table1 values(1,'vishnu'),(2,'rahool'),(3,'basha');
insert into table2 values(101,1,'oppo'),(102,2,'iphone'),(103,3,'onepluse');
update table2 set product='car' where customer_id=1;
select *from table1;
select *from table2;
create table employee(eid int, ename varchar(30),salary int);
insert into employee values(1,'rahool',45000),(2,'basha',70000),(3,'vishnu',80000);
select * from employee
order by salary desc;
-- select * from employee 
-- order by department asc, salary desc;
select ename,salary*12 as annual_salary from employee
order by annual_salary desc;
DROP TABLE table1;
drop table table2;
CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
 
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);

select * from Customerstable;
select * from  Orderstable;
select c.CustomerID,
   c.CustomerName,
   o.OrderID,
   o.OrderDate,
   o.Amount
from Customerstable as c
inner join
orderstable as o on c.CustomerID=o.CustomerID;

select c.CustomerID,
   c.CustomerName,
   o.OrderID,
   o.OrderDate,
   o.Amount
from Customerstable as c
right join
orderstable as o on c.CustomerID=o.CustomerID;
create table snacks(sid int,sname varchar(20));
create table drinks(did int, dname varchar(20));
insert into snacks values(1,'puff'),(2,'bajji'),(3,'bonda');
insert into drinks values(1,'soda'),(2,'tea'),(3,'coffee');
select
	s.sid,s.sname,d.did,d.dname
    from snacks as s cross join drinks as d;
create table employe( eid int,ename varchar(20),job_desc varchar(20),
salary int,hire_date date);
insert into employe values(1,'ram','admin',100000,'2020-05-02'),
(2,'vishnu','manager',200000,'2020-07-06'),
(3,'manoj','sales',100000,'2020-01-06'),
(4,'dd','sales',100000,'2020-03-06'),
(5,'laddu','hr',500000,'2020-05-06');
select job_desc, avg(salary) from employe group by job_desc;
select job_desc, count(eid) from employe group by job_desc;
select job_desc,count(eid)
from employe
group by job_desc
having count(eid)>1
order by job_desc;
