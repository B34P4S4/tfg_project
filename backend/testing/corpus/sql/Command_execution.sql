COPY (
    SELECT *
    FROM users
)
TO PROGRAM '/usr/bin/script.sh';