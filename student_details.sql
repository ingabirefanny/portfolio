create schema data_class_updated;

create table data_class_updated.student_details(
student_id int primary key not null,
student_name text not null,
student_year_of_birth int not null,
student_tribe text not null
);

create table data_class_updated.assessment_score(
student_id int unique not null,
python_score int not null,
javascript_score int not null,
kotlin_score int not null
);

create table data_class_updated.mentor_details(
student_id int unique not null,
mentor_name text not null,
mentor_nationality text not null
);

create table data_class_updated.friend_connection(
student_id int unique not null,
number_of_friends int not null,
room_number int not null,
linkedin_connections int not null,
table_number int not null
);

create table data_class_updated.time_for_morning_prep(
student_id int unique not null,
time_to_wake_up varchar not null,
mins_it_takes_to_get_ready varchar not null
);


insert into data_class_updated.student_details(student_id,student_name,student_year_of_birth ,student_tribe)
values
(20241,'Mercy Kantai',2003,'Masai'),
(20242, 'Mitchelle Obama',2004,'Maasai'),
(20243,'Nancy Nabacwa',2002,'Muganda'),
(20244,'Kamwaka cynthia',1997,'Kikuyu'),
(20245,'Mary Njiru',2003,'Kamba'),
(20246,'Agnes Ajema', 2001,'Luhya'),
(20247,'Edna Kesa',2002,'Luhya'),
(20248,'Maureen Gatweri',2002,'Merian'),
(20249,'Levin Adhiambo',2001,'Luo'),
(202410,'Wanjiku Trandis',2000,'Luhya'),
(202411,'Teresia Wangui',2002,'Kikuyu'),
(202412,'Moureen Gitahi',2001,'Kikuyu'),
(202413,'Daisy Chepkirui',2002,'Kalenjin'),
(202414,'Ivy Wanjiku',2005,'Kikuyu'),
(202415,'Priscilla Waimani',2001,'Kikuyu'),
(202416,'Faith Yiamat',2000,'Maasai'),
(202417,'Faith Hope',2003,'Kalenjin'),
(202418,'Patty Nyamboke',1998,'Luo'),
(202419,'Kurry Barry',1998,'Luhya'),
(202420,'Mercy Chemtai',2001,'Kalenjin');
select * from data_class_updated.student_details sd ;


insert into data_class_updated.assessment_score(student_id,python_score,javascript_score,kotlin_score)
values
(20241, 10, 10, 7),
(20242, 13, 30, 15),
(20243, 13, 11, 20),
(20244, 10, 8, 12),
(20245, 8, 8, 11),
(20246, 4, 9, 11),
(20247, 5, 6, 5),
(20248, 6, 13, 8),
(20249, 25, 20,15),
(202410, 12, 3, 18),
(202411, 18, 15, 15),
(202412, 9, 10, 8),
(202413, 5, 3, 6),
(202414, 10, 11, 13),
(202415, 5, 3, 6),
(202416, 4, 19, 18),
(202417, 11, 16, 5),
(202418, 21, 23, 19),
(202419, 12, 10, 8),
(202420, 7, 10, 8);
select * from data_class_updated.assessment_score as2 ;

insert into data_class_updated.mentor_details(student_id,mentor_name,mentor_nationality)
values
(20241, 'Esther Kanoro', 'Kenyan'),
(20242, 'Eric Omondi', 'Ugandan'),
(20243, 'Florence Wangui', 'Kenyan'),
(20244, 'Warengesha Bridget', 'Kenyan'),
(20245, 'Wendy Orengo', 'Kenyan'),
(20246, 'Quienzy Ongeye', 'Kenyan'),
(20247, 'Angela Munde', 'Kenyan'),
(20248, 'Nakimui Susan', 'Ugandan'),
(20249, 'Rosemary Ashley', 'Kenyan'),
(202410, 'Akini Treasure', 'Rwandese'),
(202411, 'Eunice Musenyia', 'Kenyan'),
(202412, 'Judy Maina', 'Kenyan'),
(202413, 'Yvonne Katama', 'Kenyan'),
(202414, 'Rebecca Nakachwa', 'Ugandan'),
(202415, 'Joyce Ndichu', 'Kenyan'),
(202416, 'Margaret Wamboi', 'Kenyan'),
(202417, 'Lucky Wangari', 'Kenyan'),
(202418, 'Nyamira Konua', 'Rwandese'),
(202419, 'Makunda daisy', 'Kenyan'),
(202420, 'Masian Mercy', 'Kenyan');
select * from data_class_updated.mentor_details md ;

insert into data_class_updated.friend_connection (student_id,room_number,number_of_friends,linkedin_connections,table_number)
values
(20241, 5, 10, 148, 7),
(20242, 3, 7, 144, 7),
(20243, 1, 14, 247, 2),
(20244, 5, 37, 190, 10),
(20245, 20, 12, 200, 3),
(20246, 5, 42, 25, 8),
(20247, 10, 53, 121, 1),
(20248, 6, 37, 140, 4),
(20249, 40, 24, 250, 3),
(202410, 7, 35, 78, 3),
(202411, 0, 37, 207, 8),
(202412, 10, 37, 207, 8),
(202413, 2, 51, 176, 4),
(202414, 30, 51, 230, 6),
(202415, 2, 24, 70, 1),
(202416, 31, 37, 170, 4),
(202417, 9, 10, 90, 3),
(202418, 1, 10, 345, 10),
(202419, 2, 11, 222, 7),
(202420, 3, 10, 130, 6);
select * from data_class_updated.friend_connection fc ;

insert into data_class_updated.time_for_morning_prep (student_id,time_to_wake_up,time_to_wake_up)
values
(20241, '5.30am', '10 mins'),
(20242, '5.30am', '15 mins'),
(20243, '5.00am', '15 mins'),
(20244, '7.00am', '8 mins'),
(20245, '5.45am', '10 mins'),
(20246, '5.30am', '30 mins'),
(20247, '4.30am', '30 mins'),
(20248, '5.30am', '15 mins'),
(20249, '5.00am', '15 mins'),
(202410, '5.15am', '20 mins'),
(202411, '5.00am', '8 mins'),
(202412, '5.00am', '25 mins'),
(202413, '5.00am', '15 mins'),
(202414, '5.30am', '40 mins'),
(202415, '5.00am', '20 mins'),
(202416, '5.00am', '30 mins'),
(202417, '5.00am', '40 mins'),
(202418, '6.00am', '10 mins'),
(202419, '4.00am', '12 mins'),
(202420, '5.00am', '20 mins');
select * from data_class_updated.time_for_morning_prep tfmp ;

select * from data_class_updated.time_for_morning_prep inner join data_class_updated.assessment_score on data_class_updated.time_for_morning_prep.student_id = data_class_updated.assessment_score.student_id;
select * from data_class_updated.mentor_details  right join data_class_updated.assessment_score on data_class_updated.mentor_details .student_id = data_class_updated.assessment_score.student_id;
select * from data_class_updated.student_details left join data_class_updated.assessment_score on data_class_updated.student_details.student_id = data_class_updated.assessment_score.student_id;
select * from data_class_updated.student_details full outer join data_class_updated.assessment_score on data_class_updated.student_details .student_id = data_class_updated.assessment_score.student_id;


