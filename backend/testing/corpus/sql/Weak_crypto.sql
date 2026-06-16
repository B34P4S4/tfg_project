INSERT INTO Users(
    username,
    password_hash
)
VALUES(
    'admin',
    MD5('Password123')
);