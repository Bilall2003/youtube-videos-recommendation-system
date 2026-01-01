 create database youtube_trending;
 use youtube_trending;
 
select * from data_info;

drop table data_info;

SELECT COUNT(*) FROM data_info WHERE description =' ';


SELECT user, host, plugin FROM mysql.user;

CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'AppPass123';
GRANT ALL PRIVILEGES ON your_db.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;

select * from data_info_clean where Cluster_Name="Viral Superstars";
select * from data_info_clean where Video_title="WE WANT TO TALK ABOUT OUR MARRIAGE";

