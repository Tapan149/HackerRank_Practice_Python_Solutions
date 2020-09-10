Hacker Rank Problems:-
1. Find city names having max length and minimum length?
 
--> select city, Length from (SELECT city, LENGTH(city) AS Length FROM station ORDER BY LENGTH(city),city ASC) where rownum=1;
    select city, Length from (SELECT city, LENGTH(city) AS Length FROM station ORDER BY LENGTH(city) DESC) where rownum=1;

2. Find city names starting with vowels?

--> select distinct city from station where REGEXP_LIKE(LOWER(city),'^[aeiou]');

3. Find city names ending with vowels?

--> select distinct city from station where REGEXP_LIKE(LOWER(city),'[aeiou]$');

4. Find city names starting and ending with vowels?

--> select distinct city from station where REGEXP_LIKE(LOWER(city),'^[aeiou]') and  REGEXP_LIKE(LOWER(city),'[aeiou]$');

5. Find city names not starting with vowels?

--> select distinct city from station where city not in 
(select distinct city from station where REGEXP_LIKE(LOWER(city),'^[aeiou]'));

6. Find city names not ending with vowels?

select distinct city from station where city not in 
(select distinct city from station where REGEXP_LIKE(LOWER(city),'[aeiou]$'));

7. Find city names neither starting with vowels nor ending with vowels?

--> select distinct city from station where city not in 
(select distinct city from station where  REGEXP_LIKE(LOWER(city),'^[aeiou]') and REGEXP_LIKE(LOWER(city),'[aeiou]$'));

8. Find city names do not start with vowels and do not end with vowels?

--> select distinct city from station where city not in 
(select distinct city from station where  REGEXP_LIKE(LOWER(city),'^[aeiou]') or REGEXP_LIKE(LOWER(city),'[aeiou]$'));

9.Query the Name of any student in STUDENTS who scored higher than 75 Marks. 
Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), 
secondary sort them by ascending ID.

--> select name from (select name,SUBSTR(name,-3) as last from students where marks>75 order by last,id);

10. Query a count of the number of cities in CITY having a Population larger than 100000. (Revising Aggregations - The Count Function)

-->

calculate difference between actual avg salary and miscalculated avg salary (i.e. salaries taken with out zeros in value).

--> SELECT CEIL((AVG(salary)) - (AVG(REPLACE(salary, '0', '')))) FROM employees;

11. Display maximum earning(i.e. salary*months) and no. of employees getting maximum earning. (Top Earner)

--> select max(salary*months),count(*) from employee where (salary*months)=(select max(salary*months) from employee) ;

12. Display Rounded values of sum of Lat_n and Long_w column in station table. (Weather Observation Station 2)

--> select round(sum(lat_n),2),round(sum(long_w),2) from station;

13. Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.
    oracle---
--> SELECT ROUND(MAX(LONG_W),4)
    FROM STATION
    WHERE LAT_N=(SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345);

or> MySql---
   SELECT ROUND(LONG_W, 4)
   FROM STATION
   WHERE LAT_N < 137.2345
   ORDER BY LAT_N DESC
   LIMIT 1;

14. Find the distance between P1(a,b) and P2(a,b)

--> SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N))+ ABS(MAX(LONG_W) - MIN(LONG_W)), 4)
FROM STATION;



