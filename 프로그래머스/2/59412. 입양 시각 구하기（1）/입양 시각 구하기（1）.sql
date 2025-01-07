select
    hour(DATETIME) AS HOUR,
    count(*) AS COUNT
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 20
group by HOUR
order by HOUR;