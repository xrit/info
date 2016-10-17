drop table artists;

create table artists (
id int primary key,
name varchar(20),
mgr_id int
);

insert into artists (id,name) values (1,'Shirley');
insert into artists (id,name,mgr_id) values (2,'Lucy',1);
insert into artists (id,name,mgr_id) values (3,'Pat',2);
insert into artists (id,name,mgr_id) values (4,'Kim',2);
insert into artists (id,name,mgr_id) values (5,'Rie',1);
insert into artists (id,name,mgr_id) values (6,'April',5);

select * from artists;

select a.mgr_id, m.name, count(*) num_of_dir_rpt 
from artists a join artists m on (m.id = a.mgr_id)
group by a.mgr_id, m.name
order by a.mgr_id;


