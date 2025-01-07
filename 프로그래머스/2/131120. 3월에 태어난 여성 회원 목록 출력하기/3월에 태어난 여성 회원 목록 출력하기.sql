SELECT
    member_id AS MEMBER_ID,
    member_name AS MEMBER_NAME,
    gender AS GENDER,
    DATE_FORMAT(date_of_birth, "%Y-%m-%d") AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(date_of_birth) = 3
    AND gender = 'W'
    AND tlno IS NOT null
ORDER BY member_id ASC;