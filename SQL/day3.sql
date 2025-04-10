use dataanalytics;
select * from employee;
select ename from employee where salary<
(select avg(salary) from employee);
select ename,salary from employee where salary>
(select avg(salary) from employee);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'HR');
INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);
 select employee_id from employees where department_id=
 (select department_id from departments where department_name='sales');
 
SELECT e.employee_name, 
       (SELECT d.department_name 
        FROM departments d 
        WHERE d.department_id = e.department_id) AS department_name
FROM employees e
WHERE e.department_id = (
    SELECT d.department_id 
    FROM departments d 
    WHERE d.department_name = 'Sales'
);
select employee_name,department_id from employees
where department_id in
(select department_id from employees group by department_id
having count(*)>1);

select department_name from departments d
where department_id in
(select department_id from employees 
group by department_id
 having count(*)>=1
 );
insert into departments values(4,'training');
-- select department_name from departments 
-- where department_id not in
-- (select department_id from employees
-- where department_id=4);
select department_id
from employees
group by department_id
having avg(employee_id)>102;
select department_id from employees where 
department_id>(select department_id from employees where employee_id=102);
select ucase('hello world') as uppercase;
select lcase("hello world") as lowercase;
select mid('hello world',4,5) as substring;
select length('hello world') as stringlength;
select round(1560.44444,2) as roundvalue;
select now() as currentdatetime;
select format(1234.1234,2) as format_number;
select employee_name,length(employee_name) as length from employees;

-- create SEQUENCE example_1
-- as int
-- start with 10
-- increment by 10;
select * from departments;
create table nulll
(id int,cname varchar(20),ccode varchar(20));
insert into nulll values
(1,'john',null),
(2,'mith','code10');
select id,cname,coalesce(ccode,'DEFAULT')AS code1 from nulll;
start transaction;
savepoint point;
insert into  nulll values(3,'smith','code60');
select * from nulll;
rollback to point;
commit;
start transaction;
savepoint p1;
insert into nulll values
(19,'bash','code99'),
(110,'rahool','code15');
rollback to p1;

set @user_name='';
call getusername(1,@userName);
select @userName;

delimiter //
create procedure getallusers()
begin
	select * from users;
end;
//
call getallusers();

delimiter $$
create procedure getUserDetails(in  userid int)
begin
	select cid,name from customer
    where cid=userid;
end ;
$$
call getUserDetails(2);

delimiter //
create procedure info(in uid int,out username varchar(20))
begin
 select ename into username
 from employee
 where eid=uid;
end;
//

set @user_name='';
call info(1,@username);
select @username;


















