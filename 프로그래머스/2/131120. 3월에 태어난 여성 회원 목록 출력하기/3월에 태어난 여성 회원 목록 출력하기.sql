select
    member_id AS MEMBER_ID,
    member_name AS MEMBER_NAME,
    gender AS GENDER,
    DATE_FORMAT(date_of_birth, "%Y-%m-%d") AS DATE_OF_BIRTH
from member_profile
where month(date_of_birth) = 3
    and gender = 'W'
    and tlno is not null
order by member_id asc;