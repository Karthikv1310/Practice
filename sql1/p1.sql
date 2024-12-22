drop database if exists college;
create database college;
use college;
create table stud_details(sno int auto_increment primary key,stud_name varchar(20),stud_age int,stud_gender char(1),stud_email varchar(20),stud_phone bigint);
insert into stud_details(stud_name,stud_age,stud_gender,stud_email,stud_phone) values("Karthik.V",18,"M","test@test.com",9807846372),("John",18,"M","new@new.com",9584737382);
desc stud_details; #to see the table structure
select *from stud_details; #for to select and see all elements
select stud_name,stud_age,stud_gender,stud_email,stud_phone from stud_details; #to select and see each elements
select stud_name from stud_details; #single element selecting
select stud_name from stud_details where stud_age>18; #result empty since no element grater than 18
select stud_name from stud_details where stud_name like "j%"; #also v can use __ or start% or %end #like condition
select stud_name from stud_details order by stud_phone; #order by for sorting
